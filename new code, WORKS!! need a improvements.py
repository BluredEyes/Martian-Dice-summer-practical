 ## Ураа он пашет,но я засыпаю,продолжаем разработку, надо доделать с json оптимизировать крутки кибика чтобы при 2 оставшихся кбках он не играл до бесконечности а уменьшал до 1 кубика и до 0 и заканчивал ход
import random
import json

class DiceGame:
    def __init__(self):
        self.dice_count = 13
        self.player_score = 0
        self.ai_score = 0
        self.player_moves = []
        self.ai_moves = []
        self.tanks = []
        self.death_rays = []

    def roll_dice(self):
        """Rolls all the dice and returns the results."""
        results = []
        for _ in range(self.dice_count):
            result = random.randint(1, 6)
            results.append(result)
            if result == 4:
                self.tanks.append(result)
        return results

    def player_turn(self, results):
        """Handles the player's turn."""
        print("Dice Results:", results)
        self.tanks = [result for result in results if result == 4]
        print("Tanks:", self.tanks)
        print("Choose a side (1, 2, 3, 5, or 6):")
        choice = input()
        self.player_moves.append(choice)

        if choice in ['1', '2', '3']:
            self.player_score += results.count(int(choice))
            if results.count(1) and results.count(2) and results.count(3):
                self.player_score += 3
        elif choice in ['5', '6']:
            self.death_rays.extend([result for result in results if result in [5, 6]])

        results = [result for result in results if str(result) != choice]
        self.dice_count = len(results)

    def ai_turn(self, results):
        """Handles the AI's turn."""
        print("AI Dice Results:", results)
        self.tanks = [result for result in results if result == 4]
        print("AI Tanks:", self.tanks)

        # AI decision logic (replace with your desired strategy)
        choice = random.choice(['1', '2', '3', '5', '6'])
        self.ai_moves.append(choice)

        if choice in ['1', '2', '3']:
            self.ai_score += results.count(int(choice))
            if results.count(1) and results.count(2) and results.count(3):
                self.ai_score += 3
        elif choice in ['5', '6']:
            self.death_rays.extend([result for result in results if result in [5, 6]])

        results = [result for result in results if str(result) != choice]
        self.dice_count = len(results)

    def calculate_scores(self):
        """Calculates final scores and determines the winner."""
        if sum(self.tanks) > sum(self.death_rays):
            print("Player wins! No points for AI.")
            self.ai_score = 0
        else:
            print("AI wins!")

        print("Player Score:", self.player_score)
        print("AI Score:", self.ai_score)

    def play_game(self):
        """Plays the game until the end."""
        while self.dice_count > 0:
            results = self.roll_dice()
            print(f"Dice Count: {self.dice_count}")
            self.player_turn(results.copy())
            self.ai_turn(results.copy())

        self.calculate_scores()

        # Save game data to JSON
        game_data = {
            "player_score": self.player_score,
            "ai_score": self.ai_score,
            "player_moves": self.player_moves,
            "ai_moves": self.ai_moves
        }
        with open("game_data.json", "w") as f:
            json.dump(game_data, f, indent=4)

if __name__ == "__main__":
    game = DiceGame()
    game.play_game()