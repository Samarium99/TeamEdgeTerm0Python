import random
game = False
points = 0
play = str(input("I'm boooored. \nWould you like to play 'Guess a Number'? \nBut, if you get -10 points, I'M LEAVING.\n\n"))
if play in ["yes", "ya", "yessir", "yeah", "yah", "sure", "yea", "okay", "k", "ok"]:
    game = True

while game == True:
    x = random.randint(1,10)
    print("I'm thinking of a number from 1 to 10.")
    player = int(input("What is it? \n"))
    if int == x:
        print(f"You are correct, the answer is {x}!\n")
        points += 5
        print(f"You have {points} points!\n")
        if points >= 10:
            print(f"\nYou're kind of really good at this game! YOU WON\nYou ended the game with {points} points.")
            break
    elif int != x:
        print(f"You were wrong, the answer was {x}! :( womp womp\n")
        points -= 1
        print(f"You have {points} points!\n")
        if points <= -10:
            print(f"\nYou really suck at this game, go do something better >:(\nYou ended the game with {points} points.")
            break
    else:
        print("I don't know what you mean, please try again.\n")
    game = False
    play = str(input("Would you like to play again? \n"))
    if play in ["yes", "ya", "yessir", "yeah", "yah", "sure", "yea", "okay", "k", "ok"]:
        game = True
else:
    print("OK, cya!")