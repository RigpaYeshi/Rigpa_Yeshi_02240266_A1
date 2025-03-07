def rock_paper_scissore():
    import random
    print("Let's start the rock, paper, scissor game")
    print("Now you can choose any one from the following [rock, paper, scissor]")
    player =input("Player's your choice is " )
    player = player.lower()
    computer = random.choice(["rock", "paper", "scissor"])
    print(f"Computer choice is {computer}")
    if player == computer:
        return "It's a tie"
    if is_win(player, computer):
        return "You won"
    return "You lost"  
def is_win(player, opponent):
    if (player == "rock" and opponent == "scissor") or (player == "scissor" and opponent == "paper") or (player == "paper" and opponent == "rock"):
        return True 
print(rock_paper_scissore())


