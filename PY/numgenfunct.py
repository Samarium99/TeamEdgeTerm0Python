import random
# reseting the game (points reset and turning game off)
game = False
points = 0
#------------ defining functions ----------
# a function generates a random integer that's between 1 and the max_value.
def generate_random_number(max_value):
    global x
    x = random.randint(1,max_value)
    print(f"I'm thinking of a number from 1 to {max_value}.\n")
# prompts user for guess 
def get_user_guess():
    global player
    player = int(input("What is it? \n"))
# check if the answer given was correct
def check_validity():
    global x
    global points
    global player
    if player == x:
        print(f"You are correct, the answer is {x}!\n")
        points += 5
        print(f"You have {points} points!\n")
        if points >= 10:
            print(f"\nYou're kind of really good at this game! YOU WON\nYou ended the game with {points} points.")
    elif player != x:
        print(f"You were wrong, the answer was {x}! :( womp womp\n")
        points -= 1
        print(f"You have {points} points!\n")
        if points <= -10:
            print(f"\nYou really suck at this game, go do something better >:(\nYou ended the game with {points} points.")
    else:
        print("I don't know what you mean, please try again.\n")
# confirms that the user wants to play the game
def confirm_play():
    play = str(input(v))
    true = ["yes", "ya", "yessir", "yeah", "yah", "sure", "yea", "okay", "k", "ok"]
    if play in true:
        global game
        game = True
    else:
        print("I see...")

#------------------ game code ---------------
# ask player if they want to play
v = "\n\nI'm boooored. \n\nWould you like to play 'Guess a Number'? \nBut, if you get -10 points, I'M LEAVING.\n"
confirm_play()

while game == True:
    # ask player for max_value
    max_value = int(input("Okay! The number generated will be between 1 and x. \n Please enter the value of x: \n"))

    generate_random_number(max_value)
    get_user_guess()
    check_validity()
    game = False
    v = "Would you like to play again? \n"
    confirm_play()
else:
    print("OK, cya!")
