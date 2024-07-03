class PlayerInteractions #pink/white {
  choose_dices([rolled], [side], score, other_scores) -> str{side}
}

class Human #pink {
  choose_dices([rolled], [side], score, other_scores) -> str{side}
}
Human <|-- PlayerInteractions
