import unittest

class TestPlayerInteractions(unittest.TestCase):

    def test_choose_dices(self):
        player = PlayerInteractions()
        rolled = [1, 2, 3, 4, 5]
        side = "left"
        score = 10
        other_scores = [5, 8, 12]
        self.assertEqual(player.choose_dices(rolled, side, score, other_scores), side)

    def test_human_choose_dices(self):
        human = Human()
        rolled = [1, 2, 3, 4, 5]
        side = "left"
        score = 10
        other_scores = [5, 8, 12]
        self.assertEqual(human.choose_dices(rolled, side, score, other_scores), side)
