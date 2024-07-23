import random
yourScore = 0
opScore = 0
print("This is a rock-paper-scissors game, best of three.")
i = 0
while i < 4:
    firstMove = str(input("Make your move now. rock, paper, or scissors. \n"))
    moves = ("rock", "paper", "scissors")
    secondMove = random.choice(moves)
#if player chooses rock
    if firstMove == "rock":
        if secondMove == "rock":
            print(f"Your opponent chose: {secondMove}, it's a draw.")
        elif secondMove == "paper":
            print(f"Your opponent chose: {secondMove}, YOU LOSE, AHAHAHA!")
            opScore = opScore + 1
        elif secondMove == "scissors":
            print(f"Your opponent chose: {secondMove}, you win! yippee.")
            yourScore = yourScore + 1
#if player chooses paper
    elif firstMove == "paper":
        if secondMove == "rock":
            print(f"Your opponent chose: {secondMove}, you win! That's kinda cool.")
            yourScore = yourScore + 1
        elif secondMove == "paper":
            print(f"Your opponent chose: {secondMove}, that's a draw.")
        elif secondMove == "scissors":
            print(f"Your opponent chose: {secondMove}, aaaaand that's another loss for you.")
            opScore = opScore + 1
#if player chooses scissors
    elif firstMove == "scissors":
        if secondMove == "rock":
            print(f"Your opponent chose: {secondMove}, woah you won...how??")
            yourScore = yourScore + 1
        elif secondMove == "paper":
            print(f"Your opponent chose: {secondMove}, lolll draw.")
        elif secondMove == "scissors":
            print(f"Your opponent chose: {secondMove}, YA LOSE!")
            opScore = opScore + 1
#if player types something else
    else: 
        print("An error occurred, please try again.")
    i += 1
    if i == 3:
        break
#winner winner chicken dinner?
if yourScore > opScore:
    print("\n WOAH YOU WON --- VICTORY!!!!")
else:
    print("\n YOU LOST!!! VICTORY IS MINEEEEE >:)")


