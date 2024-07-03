
from dataclasses import dataclass
from typing import List

@dataclass
class GameState:
    players: List['Player']
    current_player: int
    rolled_dice: List['Dice']
    side_dice: List['Dice']

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def side_dices(self, side: str):
        return [dice for dice in self.side_dice if dice.side == side]

    def score(self) -> int:
        # Implement score calculation logic
        pass

    def save(self) -> str:
        # Implement saving logic
        pass

    def load(self, json: str):
        # Implement loading logic
        pass
