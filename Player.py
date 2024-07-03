from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Player:
    name: str
    score: int
    type: "PlayerInteraction"

    def choose_dices(self, available_dices: List[int], num_dices: int) -> List[int]:
        """
        Choose dices to roll.

        Args:
            available_dices: List of available dices to choose from.
            num_dices: Number of dices to choose.

        Returns:
            List of chosen dices.
        """
        chosen_dices = []
        while len(chosen_dices) < num_dices:
            dice = input(f"Choose a dice from {available_dices}: ")
            if dice in available_dices:
                chosen_dices.append(dice)
                available_dices.remove(dice)
            else:
                print("Invalid dice choice.")
        return chosen_dices

    def save(self) -> str:
        """
        Save player data to JSON.

        Returns:
            JSON string representing player data.
        """
        return {
            "name": self.name,
            "score": self.score,
            "type": self.type.value
        }

    def load(self, json: str):
        """
        Load player data from JSON.

        Args:
            json: JSON string representing player data.
        """
        self.name = json["name"]
        self.score = json["score"]
        self.type = PlayerInteraction(json["type"])

