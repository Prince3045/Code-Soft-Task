import random

class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        while True:
            print("\nChoose one:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice = input("Enter your choice (1/2/3): ")

            if choice in ['1', '2', '3']:
                return self.choices[int(choice) - 1]
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_game(self):
        print("Welcome to Advanced Rock, Paper, Scissors Game!")

        rounds = int(input("Enter number of rounds you want to play: "))
        
        for _ in range(rounds):
            print(f"\nPlayer: {self.player_score} | Computer: {self.computer_score}")
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            result = self.determine_winner(player_choice, computer_choice)
            print(result)

        print("\nFinal Scores:")
        print(f"Player: {self.player_score} | Computer: {self.computer_score}")

        if self.player_score > self.computer_score:
            print("Congratulations! You win the game!")
        elif self.player_score < self.computer_score:
            print("Computer wins the game!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = RPSGame()
    game.play_game()
