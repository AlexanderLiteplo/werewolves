from typing import List
from types_1 import GameState, GameRole
from llm import LLMInterface
import tiktoken

class SimpleAgent:
    def __init__(self, llm: LLMInterface, name: str, role: GameRole, game_state: GameState):
        self.name = name
        self.role = role
        self.llm = llm
        self.game_state = game_state
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def prompt(self, chat_history: List[str]) -> str:
        system_prompt = self._initialize_system_prompt(self.game_state.phase, self.game_state.get_role_counts())

        return system_prompt + self.game_state.format_state() + "\n\n" + "\n".join(chat_history)
    
    def _count_tokens(self, text: str) -> int:
        """Count tokens in a text string"""
        return len(self.tokenizer.encode(text))

    def _initialize_system_prompt(self, phase: str = "day", players_alive: int = 0):
        """Set up the initial system prompt for the agent"""
        system_prompt = self.SYSTEM_PROMPT.format(
            role=self.game_role.value,
            role_objectives=self.ROLE_OBJECTIVES[self.game_role],
            phase=phase,
            players_alive=players_alive
        )
        self.memory.append(Message(role="system", content=system_prompt))
        