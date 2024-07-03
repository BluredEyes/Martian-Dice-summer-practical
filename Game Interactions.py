from dataclasses import dataclass

@dataclass
class GameInteractions:
    def run(self):
        pass

    def load(self, json):
        pass

    def request_players(self) -> list['Player']:
        pass

    def print_rolled_dice(self, dices: list['Dice']):
        pass

    def print_side_dice(self, dices: list['Dice']):
        pass

    def print_player_info(self, player: 'Player'):
        pass
