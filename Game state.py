class GameState #lightblue {
  players : [Player]
  current_player : int
  rolled_dice : [Dices]
  side_dice : [Dices]
  ==
  next_player()
  side_dices(str{side})
  score() -> int
  ..
  save() -> json
  load(json)
}
GameState o-- Player
GameState o-- Dice
