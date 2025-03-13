import random
def game_selection():
    print("Hello, Welcome to the game ")
    print("Select a function(1-3)")
    print("1. Guess the number \n2. Rock paper scissors game \n3. Exit Program")

    game = int(input("Enter your choice : "))
    if game == 1:
        print("You have selected Guess the number game")
        number = random.randint (1, 20)
        attempt = 0
        while True:
            try:
                guess = int(input("Guess a number: "))
                if guess < 1 or guess > 20:
                    print("Enter a number between 1 and 20")
                    continue
                attempt += 1
                if guess < number:
                    print("Too low")
                elif guess > number :
                    print("Too high")
                else:
                    print("You got it in", attempt, "attempts")
                    break
            except ValueError:
                print("Enter a valid number")
    
    elif game == 2:
        print("You have selected Rock paper scissors game")
        print("Welcome to the Rock Paper Scissor game")
        print("1. Rock \n2. Paper \n3. Scissor")
        attempts = 0
        while True:
            computer = random.choice(["rock", "paper", "scissor"])
            player = input("Enter your choice: ")
            attempts += 1
            if player not in ["rock", "paper", "scissor"]:
              print("Invalid choice, try again")
              continue
            else:
                print(f"Computer choice is {computer}")
                if player == computer:
                    print("It's a tie")
                elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
                    print("You won")
                else:
                    print("You lost")
                play_again = input("Do you want to play again? [yes/no]: ")
                if play_again == "yes":
                    continue
                else:
                    print("You played", attempts, "times")
                    print("Thanks for playing")
                    break
    elif game == 3:
        print("You have chosen to exit")
    else:
        print("Invalid choice")
game_selection()
            

