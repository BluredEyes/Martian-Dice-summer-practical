import unittest
from unittest.mock import patch

class TestGameInteractions(unittest.TestCase):

    @patch('main.GameInteractions.request_players')
    @patch('main.GameInteractions.load')
    def test_run(self, mock_load, mock_request_players):
        game = GameInteractions()
        mock_load.return_value = None
        mock_request_players.return_value = []
        game.run()
        mock_load.assert_called_once()
        mock_request_players.assert_called_once()

    @patch('main.GameInteractions.print_rolled_dice')
    @patch('main.GameInteractions.print_side_dice')
    @patch('main.GameInteractions.print_player_info')
    def test_print_game_info(self, mock_print_player_info, mock_print_side_dice, mock_print_rolled_dice):
        game = GameInteractions()
        mock_print_rolled_dice.return_value = None
        mock_print_side_dice.return_value = None
        mock_print_player_info.return_value = None
        game.print_rolled_dice(None)
        game.print_side_dice(None)
        game.print_player_info(None)
        mock_print_rolled_dice.assert_called_once()
        mock_print_side_dice.assert_called_once()
        mock_print_player_info.assert_called_once()
