import random
import Rigpa_Yeshi_02240266_A2_PB as pb
class OverallScore:
    """
    Class to maintain overall scores for all games.
    """
    def __init__(self):
        self.scores = {
            "guess_number": 0,
            "rock_paper_scissors": 0,
            "trivia": 0,
            "pokemon_cards": 0
        }

    def add_score(self, game, points):
        self.scores[game] += points

    def display(self):
        print("Overall Scores:")
        for game, score in self.scores.items():
            print(f"{game}: {score}")

class GuessNumberGame:
    """
    Guess Number Game
    User guesses a random number between a range.
    Score = Number of valid numbers - number of guesses with minimum 0
    """
    def __init__(self, overall_score):
        self.overall_score = overall_score

    def play(self):
        number_to_guess = random.randint(1, 20)
        guesses = 0
        valid_guesses = 0
        print("Welcome to the Guess Number Game! \nGuess a number between 1 and 20.")
        while True:
            try:
                guess = int(input("Enter your guess (or 0 to quit): "))
                if guess == 0:
                    print("Quitting Guess Number Game.")
                    break
                guesses += 1
                if 1 <= guess <= 100:
                    valid_guesses += 1
                else:
                    print("Guess must be between 1 and 100.")
                    continue
                if guess < number_to_guess:
                    print("Low")
                elif guess > number_to_guess:
                    print("High")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        score = max(0, valid_guesses - guesses)
        self.overall_score.add_score("guess_number", score)

class RockPaperScissorsGame:
    """
    Rock Paper Scissors Game
    Text-based game against a random computer opponent.
    Score = Number of wins versus computer
    """
    def __init__(self, overall_score):
        self.overall_score = overall_score

    def play(self):
        computer = ["rock", "paper", "scissors"]
        score = 0
        print("Welcome to Rock Paper Scissors Game!")
        while True:
            player = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
            if player == 'exit':
                print("Exiting Rock Paper Scissors Game.")
                break
            if player not in computer:
                print("Invalid choice. Please try again.")
                continue
            computer_choice = random.choice(computer)
            print(f"Computer chose: {computer_choice}")
            if player == computer_choice:
                print("It's a tie!")
            elif (player == "rock" and computer_choice == "scissors") or \
                 (player == "paper" and computer_choice == "rock") or \
                 (player == "scissors" and computer_choice == "paper"):
                print("You win!")
                score += 1
            else:
                print("You lose!")
        self.overall_score.add_score("rock_paper_scissors", score)

class TriviaPursuitGame:
    """
    Trivia Pursuit Game
    Multiple categories and multiple-choice questions.
    Score = Number of correct guesses
    """
    def __init__(self, overall_score):
        self.overall_score = overall_score
        self.questions = {
            "CSF": [
                ("1. Which of the following statements regarding data structures in Python is true?", ["A. Python lists are the same as traditional arrays", "B. Sets are immutable", "C. Tuples are used to store unique values", "D. Python dictionary stores data in key-value pairs."], 3),
                ("2. Which of the following statements is true regarding variable scope in Python?", ["A. Variables defined inside a function are automatically available to outer functions and the global scope.", "B. The global keyword allows a variable defined in the global scope to be modified within a function.", "C. When a variable is referenced in a function, Python first looks at the global scope before checking the local scope.", "D. The nonlocal keyword is used to access variables from the global scope within a nested function."], 1)
            ],
            "Engineering Machanics": [
                ("1. The angle between two forces when the resultant is maximum and minimum respectively are", ["0° and 180°", "90° and 180°", "0 and 90°", "90° and 0"], 0),
                ("2 Which of the following is the example of lever of first order?", ["a. Arm of man", "b. Pairs of scissors", "c. Pair of clinical tongs", "d. All of the above"], 3)
            ]
        }

    def play(self):
        score = 0
        print("Welcome to Trivia Pursuit Game!")
        for category, questions in self.questions.items():
            print(f"\nCategory: {category}")
            for question, options, correct_idx in questions:
                print(question)
                for i in range(len(options)):
                    print(f"{i + 1}. {options[i]}")
                try:
                    answer = int(input("Your answer (1-4): "))
                    if 1 <= answer <= 4:
                        if options[answer - 1] == options[correct_idx]:
                            print("Correct!")
                            score += 1
                        else:
                            print("Wrong!")
                    else:
                        print("Invalid input. Skipping question.")
                except ValueError:
                    print("Invalid input. Skipping question.")
                try:
                    answer = int(input("Your answer (1-4): "))
                    if answer == correct_idx + 1:
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong!")
                except ValueError:
                    print("Invalid input. Skipping question.")
        self.overall_score.add_score("trivia", score)

pokemon_binder = pb.PokemonBinderManager()
class PokemonCardBinderManager:
    """
    Pokémon Card Binder Manager
    Manage a collection of Pokémon cards.
    Score = Number of cards in the binder
    """
    
    def __init__(self, overall_score):
        self.overall_score = overall_score
        self.binder = pokemon_binder

    def run(self):
        print("\nWelcome to Pokémon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("1. Add Pokémon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. View score")
            print("5. Exit")
        
            try:
               option = int(input("\nSelect option (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
        
            if option == 1:
                try:
                   pokedex_num = int(input("Enter Pokedex number: "))
                   result = self.binder.add_card(pokedex_num)
                   pb.display_position_info(result, pokedex_num)
                except ValueError:
                   print("Invalid input. Please enter a valid Pokedex number.")
        
            elif option == 2:
                print("\nWARNING: This will erase all cards in your binder!")
                choice = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").upper()
                if choice == "CONFIRM":
                    result = self.binder.reset_binder()
                    print(result)
                elif choice == "EXIT":
                    continue
                else:
                   print("Invalid input. No changes made.")
        
            elif option == 3:
                result = self.binder.view_binder()
                pb.display_binder_contents(result)
        
            elif option == 4:
                print(f"\nCurrent score: {self.binder.score()} Pokémon cards")
        
            elif option == 5:
                print("Exiting Pokémon Card Binder Manager.")
                print(f"Final collection score: {self.binder.score()} Pokémon cards")
                break
        
            else:
                print("Invalid option. Please select a number between 1 and 5.")
def main():
    overall_score = OverallScore()
    guess_game = GuessNumberGame(overall_score)
    rps_game = RockPaperScissorsGame(overall_score)
    trivia_game = TriviaPursuitGame(overall_score)
    pokemon_manager = PokemonCardBinderManager(overall_score)

    while True:
        print("\nSelect a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("0. Exit program")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            guess_game.play()
        elif choice == '2':
            rps_game.play()
        elif choice == '3':
            trivia_game.play()
        elif choice == '4':
            pokemon_manager.run()
        elif choice == '5':
            overall_score.display()
        elif choice == '0':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
