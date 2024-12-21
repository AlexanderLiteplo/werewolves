from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class GameRole(Enum):
    VILLAGER = "villager"
    WEREWOLF = "werewolf"
    SEER = "seer"
    WITCH = "witch"
    HUNTER = "hunter"
    HIDDEN = "hidden"

class GamePhase(Enum):
    DAY = "day"
    NIGHT = "night"
    VOTING = "voting"
    DAY_VOTING = "day_voting"
    NIGHT_VOTING = "night_voting"

@dataclass
class PlayerInfo:
    name: str
    is_alive: bool
    role: GameRole

    
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
