class PlayerInteractions:
    def choose_dices(self, rolled, side, score, other_scores):
        return side

class Human(PlayerInteractions):
    def choose_dices(self, rolled, side, score, other_scores):
        return super().choose_dices(rolled, side, score, other_scores)
