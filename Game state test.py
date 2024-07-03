import unittest
from main import GameState, Player, Dice

class TestGameInteractions(unittest.TestCase):

    def test_next_player(self):
        game_state = GameState(
            players=[Player("Player 1"), Player("Player 2")],
            current_player=0,
            rolled_dice=[],
            side_dice=[]
        )
        game_state.next_player()
        self.assertEqual(game_state.current_player, 1)

    def test_side_dices(self):
        game_state = GameState(
            players=[],
            current_player=0,
            rolled_dice=[],
            side_dice=[
                Dice(1, "left"),
                Dice(2, "right"),
                Dice(3, "left")
            ]
        )
        left_dices = game_state.side_dices("left")
        self.assertEqual(len(left_dices), 2)
        self.assertIn(Dice(1, "left"), left_dices)
        self.assertIn(Dice(3, "left"), left_dices)

    def test_score(self):
        # Implement test logic for score calculation
        pass

    def test_save(self):
        # Implement test logic for saving
        pass

    def test_load(self):
        # Implement test logic for loading
        pass

if name == '__main__':
    unittest.main() 
