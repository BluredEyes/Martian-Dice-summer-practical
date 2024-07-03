import unittest
from main import Player, PlayerInteraction

class TestPlayer(unittest.TestCase):

    def test_choose_dices(self):
        player = Player("Test Player", 0, PlayerInteraction.HUMAN)
        available_dices = [1, 2, 3, 4, 5, 6]
        chosen_dices = player.choose_dices(available_dices, 2)
        self.assertEqual(len(chosen_dices), 2)
        self.assertTrue(all(dice in available_dices for dice in chosen_dices))

    def test_save(self):
        player = Player("Test Player", 100, PlayerInteraction.AI)
        json = player.save()
        self.assertEqual(json["name"], "Test Player")
        self.assertEqual(json["score"], 100)
        self.assertEqual(json["type"], PlayerInteraction.AI.value)

    def test_load(self):
        player = Player("Test Player", 0, PlayerInteraction.HUMAN)
        json = {"name": "Test Player", "score": 50, "type": PlayerInteraction.AI.value}
        player.load(json)
        self.assertEqual(player.name, "Test Player")
        self.assertEqual(player.score, 50)
        self.assertEqual(player.type, PlayerInteraction.AI)

if __name__ == '__main__':
    unittest.main()
