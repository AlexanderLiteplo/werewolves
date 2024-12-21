from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import tiktoken
from constants import LLMModel, TokenLimits, MODEL_CONTEXT_WINDOWS
from llm import LLM


class GameRole(Enum):
    VILLAGER = "villager"
    WEREWOLF = "werewolf"
    SEER = "seer"
    WITCH = "witch"
    HUNTER = "hunter"
    # Add more roles as needed

@dataclass
class Message:
    role: str  # "system", "user", or "assistant"
    content: str
    timestamp: datetime = datetime.now()

@dataclass
class PlayerInfo:
    name: str
    is_alive: bool
    role: Optional[GameRole] = None  # Role is revealed when dead

@dataclass
class GameState:
    players: List[PlayerInfo]
    day_number: int
    phase: str  # "day" or "night"
    
    def get_role_counts(self) -> Dict[GameRole, int]:
        """Count living players of each role (only includes known roles)"""
        counts = {role: 0 for role in GameRole}
        for player in self.players:
            if player.is_alive and player.role:
                counts[player.role] += 1
        return counts
    
    def format_state(self) -> str:
        """Format game state as a string for the LLM"""
        state = f"Game Day: {self.day_number}\nPhase: {self.phase}\n\n"
        
        # List living players
        state += "Living Players:\n"
        living = [p.name for p in self.players if p.is_alive]
        state += ", ".join(living) + "\n\n"
        
        # List dead players with their roles
        state += "Dead Players:\n"
        dead = [f"{p.name} ({p.role.value})" for p in self.players if not p.is_alive and p.role]
        state += ", ".join(dead) if dead else "None"
        
        return state

class Agent:
    SYSTEM_PROMPT = """You are playing a game of Werewolf. You are a {role}.

    Key information:
    - You must act according to your role's objectives
    - You must stay in character at all times
    - Your responses should be concise and relevant to the game
    
    As a {role}, your specific objectives are:
    {role_objectives}
    
    Current game state:
    {game_state}""" 

    ROLE_OBJECTIVES = {
        GameRole.VILLAGER: "Identify and eliminate werewolves through discussion and voting. Stay alive and protect the village.",
        GameRole.WEREWOLF: "Eliminate villagers without revealing your identity. Coordinate with other werewolves secretly.",
        GameRole.SEER: "Use your ability to see other players' roles at night. Help villagers without exposing yourself.",
        GameRole.WITCH: "Use your potions wisely - you have one healing potion and one poison potion. Help the village survive.",
        GameRole.HUNTER: "If you die, you can take one other player with you. Choose wisely who to shoot.",
    }

    def __init__(self, 
                 llm: LLM,
                 name: str, 
                 game_role: GameRole,
                 system_prompt: str,
                 max_memory_tokens: Optional[int] = None):
        """
        Initialize an AI agent for the Werewolf game
        
        Args:
            llm (LLM): The LLM instance to use for chat completions
            name (str): Player name
            game_role (GameRole): The assigned game role
            system_prompt (str): Base system prompt
            max_memory_tokens: Maximum tokens to store in memory
        """
        self.llm = llm
        self.name = name
        self.game_role = game_role
        self.base_system_prompt = system_prompt
        
        # Use model-specific context window if max_memory_tokens not specified
        self.max_memory_tokens = max_memory_tokens or MODEL_CONTEXT_WINDOWS[llm.model]
        # Reserve 20% of tokens for system prompt and response
        self.max_memory_tokens = int(self.max_memory_tokens * 0.8)
        self.memory: List[Message] = []
        
        # Initialize tokenizer based on model
        self.tokenizer = self._get_tokenizer()
        
        # Initialize with system prompt
        self._initialize_system_prompt()

    def _get_tokenizer(self):
        """Get the appropriate tokenizer based on the model"""
        if self.llm.model.value.startswith("gpt"):
            # OpenAI models
            if "4" in self.llm.model.value:
                return tiktoken.encoding_for_model("gpt-4")
            return tiktoken.encoding_for_model("gpt-3.5-turbo")
        elif "claude" in self.llm.model.value:
            # Claude models - using cl100k_base
            return tiktoken.get_encoding("cl100k_base")
        else:
            # Default to cl100k_base for other models
            return tiktoken.get_encoding("cl100k_base")

    def _count_tokens(self, text: str) -> int:
        """Count tokens in a text string"""
        return len(self.tokenizer.encode(text))

    def _get_message_tokens(self, message: Message) -> int:
        """Count tokens in a message including role overhead"""
        # Count tokens in the message content
        content_tokens = self._count_tokens(message.content)
        
        # Add overhead for message format based on OpenAI's token counting
        # Format: {"role": "role_name", "content": "message"}
        # 4 tokens for the message structure: 2 for the object wrapper, 2 for role/content keys
        role_tokens = self._count_tokens(message.role)
        format_tokens = 4
        
        return content_tokens + role_tokens + format_tokens

    def _get_messages_token_count(self, messages: List[Message]) -> int:
        """Get total token count for a list of messages"""
        return sum(self._get_message_tokens(msg) for msg in messages)

    def _initialize_system_prompt(self, phase: str = "day", players_alive: int = 0):
        """Set up the initial system prompt for the agent"""
        system_prompt = self.SYSTEM_PROMPT.format(
            role=self.game_role.value,
            role_objectives=self.ROLE_OBJECTIVES[self.game_role],
            phase=phase,
            players_alive=players_alive
        )
        self.memory.append(Message(role="system", content=system_prompt))

    def _prune_memory(self):
        """Remove oldest messages if memory exceeds token limit"""
        total_tokens = self._get_messages_token_count(self.memory)
        
        # Keep removing oldest non-system messages until under token limit
        while total_tokens > self.max_memory_tokens and len(self.memory) > 1:
            # Always keep the system message (index 0)
            # Remove the second message (index 1) which is the oldest non-system message
            removed_message = self.memory.pop(1)
            total_tokens -= self._get_message_tokens(removed_message)

    def _prune_messages(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Prune a message list to fit within token limit"""
        # Convert dict messages to Message objects for token counting
        msg_objects = [Message(role=msg["role"], content=msg["content"]) 
                      for msg in messages]
        
        total_tokens = self._get_messages_token_count(msg_objects)
        
        # Keep removing oldest non-system messages until under token limit
        while total_tokens > self.max_memory_tokens and len(messages) > 1:
            # Always keep the system message (index 0)
            # Remove the second message (index 1)
            messages.pop(1)
            msg_objects.pop(1)
            total_tokens = self._get_messages_token_count(msg_objects)
        
        return messages

    def _format_full_prompt(self, game_state: GameState) -> str:
        """Combine system prompt with current game state"""
        return f"""{self.base_system_prompt}

Current Game State:
{game_state.format_state()}

Your Role: {self.game_role.value}
Your Name: {self.name}"""

    def prompt(self, 
                    message: str, 
                    game_state: GameState,
                    chat_history: Optional[List[Message]] = None) -> str:
        """
        Send a prompt to the agent and get its response
        """
        # Format system prompt with current game state
        system_prompt = self._format_full_prompt(game_state)
        
        # Use provided chat history or internal memory
        messages_to_use = chat_history if chat_history is not None else self.memory
        
        # Prepare messages for LLM
        formatted_messages = [
            {"role": "system", "content": system_prompt},
            *[{"role": msg.role, "content": msg.content} for msg in messages_to_use],
            {"role": "user", "content": message}
        ]
        
        # Prune if needed
        formatted_messages = self._prune_messages(formatted_messages)
        
        # Get response from LLM
        response = self.llm.chat_completion(formatted_messages)
        
        # Store in internal memory if not using external chat history
        if chat_history is None:
            # Check if adding new messages would exceed token limit
            new_messages = [
                Message(role="user", content=message),
                Message(role="assistant", content=response)
            ]
            
            # Add new messages and prune if necessary
            self.memory.extend(new_messages)
            self._prune_memory()
        
        return response

    def get_memory_summary(self) -> List[Dict]:
        """Get a summary of important events from memory"""
        return [{"role": msg.role, 
                "content": msg.content, 
                "timestamp": msg.timestamp} 
                for msg in self.memory]
