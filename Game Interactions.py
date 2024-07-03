class GameInteractions #lightgreen {
  ==
  run()
  load(json)
  ..
  request_players() -> [Player]
  print_rolled_dice([Dices])
  print_side_dice([Dices])
  print_player_info(Player)
}
GameInteractions -- GameState
