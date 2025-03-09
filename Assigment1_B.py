import random

def game_start():
    print("\n WELCOME TO THE GAME\n")
    print("you can choose any one of the following options [1,2]")
    print("1. Guess the number Game")
    print("2. Rock Paper Scissor Game")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("You have chosen Guess the number Game")
        number = random.randint(1, 25)
        attempts = 0
        print("Let's start the game")
        print("Guess the number between 1 to 25")
        while True:
            try:
                number = int(input("Enter a number between 1 to 25: "))
                attempts += 1
                if number == number:
                    print(f"\n Yess!!!... , You guessed the number in {attempts} attempts \n")
                    break
                elif number < number:
                    print(" Yalama!!!... , it's too low, try again")
                else:
                    print("Yalama!!!... , it's too high, try again")
            except ValueError:
                print("The number you entered is invalid, try again")
    elif choice == 2:
        print("You have chosen Rock Paper Scissor Game")
        print("Let's start the rock, paper, scissor game")
        while True:
            player = input("Enter your choice [rock, paper, scissor]: ")
            if player not in ["rock", "paper", "scissor"]:
                print("Invalid choice, try again")
            else:
                break
        computer = random.choice(["rock", "paper", "scissor"])
        print(f"Computer choice is {computer}")
        if player == computer:
            print("NO!!!... , It's a tie")
        elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
            print("Yess!!!... , You won")
        else:
            print("oops!!!... , You lost")
    elif choice == 3:
        print("You have chosen to exit")
    else:
        print("Invalid choice")
game_start()