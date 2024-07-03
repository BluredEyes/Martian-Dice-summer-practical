import random

def ai_turn():
    """
    AI's turn logic.
    """
    dice = [1, 2, 3, 4, 5, 6] * 13
    rolls = random.choices(dice, k=13)
    tank_count = rolls.count(4)
    rolls = [x for x in rolls if x != 4]
    
    # AI selects either all faces 5 and 6 or same several faces 1 2 or 3
    if rolls.count(5) + rolls.count(6) >= rolls.count(1) + rolls.count(2) + rolls.count(3):
        selected_faces = [5, 6]
    else:
        selected_faces = [1, 2, 3]
    
    # Roll the remaining dice
    rolls = [x for x in rolls if x in selected_faces]
    rolls = random.choices(rolls, k=len(rolls))
    
    # Calculate score
    score = 0
    if tank_count <= rolls.count(5) + rolls.count(6):
        for face in [1, 2, 3]:
            score += rolls.count(face)
        if rolls.count(1) > 0 and rolls.count(2) > 0 and rolls.count(3) > 0:
            score += 3
    
    return score
