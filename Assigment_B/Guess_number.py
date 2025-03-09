def guess_number():
    import random
    number = random.randint(1, 50)
    print("Let's start the game")   
    print("Guess the number between 1 to 10")
    player = int(input("Player your choice is "))
    if player == number:
        print(f"Yess!!!... , You guessed the number {number}")  
    return "Nope!!!... , You need to guess again next time"
print(guess_number())
