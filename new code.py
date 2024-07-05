import random
import json

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tanks = 0
        self.selected_faces = []
        self.remaining_dice = 0  # Store remaining dice after a roll

    def roll_dice(self):
        if self.remaining_dice > 0:
            dice = [random.randint(1, 6) for _ in range(self.remaining_dice)]
        else:
            dice = [random.randint(1, 6) for _ in range(13)]
        tanks = dice.count(4)
        dice = [die for die in dice if die != 4]
        self.tanks += tanks
        print(f"{self.name}'s roll: {dice}, Tanks: {tanks}")
        return dice

    def choose_face(self, dice):
        while True:
            try:
                choice = int(input(f"{self.name}, choose a face (1, 2, 3, 5, 6): "))
                if choice in [1, 2, 3, 5, 6]:
                    break
                else:
                    print("Invalid choice. Please choose from 1, 2, 3, 5, or 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.selected_faces.extend([choice])  # Add the chosen face
        if choice == 5:
            self.selected_faces.extend([6])  # Automatically add 6 if 5 is chosen
        elif choice == 6:
            self.selected_faces.extend([5])  # Automatically add 5 if 6 is chosen
        return choice

    def calculate_score(self, dice, tanks):
        ones = self.selected_faces.count(1)
        twos = self.selected_faces.count(2)
        threes = self.selected_faces.count(3)
        fives = self.selected_faces.count(5)
        sixes = self.selected_faces.count(6)

        if tanks <= (fives + sixes):
            self.score += ones + twos + threes
            if ones and twos and threes:
                self.score += 3

        self.score += fives + sixes

    def play_turn(self):
        dice = self.roll_dice()
        while len(dice) > 1:
            choice = self.choose_face(dice)
            if choice == 5:
                dice = [die for die in dice if die not in [5, 6, 4]]  # Remove 5 and 6 
            elif choice == 6:
                dice = [die for die in dice if die not in [5, 6, 4]]  # Remove 5 and 6
            else:
                dice = [die for die in dice if die not in [choice, 4]]
            self.remaining_dice = len(dice)  # Update remaining dice
            print(f"Remaining dice: {self.remaining_dice}")
            dice = self.roll_dice()

        self.calculate_score(dice, self.tanks)
        print(f"{self.name}'s score: {self.score}")

    def save_data(self):
        data = {
            "name": self.name,
            "score": self.score,
            "tanks": self.tanks,
            "selected_faces": self.selected_faces
        }
        with open("game_data.json", "w") as f:
            json.dump(data, f)

class AI(Player):
    def choose_face(self, dice):
        # Simple AI: choose random face
        choice = random.choice([1, 2, 3, 5, 6])
        print(f"AI chooses: {choice}")
        self.selected_faces.extend([choice])
        if choice == 5:
            self.selected_faces.extend([6])
        elif choice == 6:
            self.selected_faces.extend([5])
        return choice

def main():
    player = Player("Player")
    ai = AI("AI")

    while player.score < 25 and ai.score < 25:
        player.play_turn()
        player.save_data()
        ai.play_turn()
        ai.save_data()

    if player.score >= 25:
        print("Player wins!")
    else:
        print("AI wins!")

if __name__ == "__main__":
    main() 
