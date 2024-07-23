# Journey Challenge:
# Create your own survival story by being creative in your story telling and create ways of surviving your simulation!
# Input at least 10 key-value pairs in your new dictionary and have more than 2 tools to help you survive!
# Make sure the conditions match with the bad and good decision making behind the template!

# BONUS: Create a functions within the program to make it more efficient and clean!


# dictionary for the tools
# backpack = {
#   "headphones": "A",
#   "lighter": "B",
#   "flashlight": "C",
#   "batteries": "D",
#   "phone": "E"
# }

# C = "Flashlight! Do you want to turn it on?"
# D = "Batteries. They charge stuff. Nice."
# E = "You check your phone. It's a beat up flip phone, a nokia to be exact. It's dead. You put it away, since it's no use as of now."


settings = {
  "hallway": "h",
  "balcony": "b"
}

def choose():
  global userChoices
  global userList
  print("Choose your option")
  userChoices = input("Insert the letters you want to choose with no spaces but with a comma between each letter: ")
  userList = list(userChoices.split(','))

def game():
  global name
  global userChoices
  global userList
  global values
  print("The room that you are in resembles a school dormitory, except all the beds are capsules...and they're hanging on the walls.\nThis saves a lot of floor space, you think to yourself.")
  name = input("In your capsule, you see your name...it reads:  ")
  
  print("Peeking out of this room, you see a hallway to your right, and a balcony to your left, overlooking the commonroom area.")

  values = settings.values() 
  # Get all key-value pairs
  items = settings.items()
  # Print each key-value pair
  for key, value in items:
    print(f"{value}: {key}")
  
  choose()

  if "h" in userList:
    print("The hallway-corridor is all clear, with two doors. There's one closest to you, and a second, that's at the end of the hall.")
  elif "b" in userList:
    print("You look over the balcony, seeing three astronauts far-down below, wearing suits the colors purple, blue, and green (color credits: Jada). You stare at them for a while, watching them move, at 1:10 scale...\nSuddenly, the one in purple turns its head at you.\n\nThe figure waves.\nYou run.")
    userList.pop["b"]
    userList.update({"hallway": "h"})


  else:
    print("Please enter ")
    choose()

def check_for_start(word):
  user_input = input("TYPE 'start' to begin...\n")
  if word in user_input:
    print("-------------------------------------------------------------------------------------")
    game()
  else:
    print("error")


#-----Actual Game Code----------------------------------------------------------------------------------------------------------#
print("\nWelcome to the journey simulator. Choose options to win and escape!")
if input("-----------------------------------------------------------(Enter anything to continue)\n"):
  print("You wake up to bright, white, fluorescent lights, and as you rubbed clarity into your eyes, you realized that you were in a space ship. You knew it was a spaceship, because you felt as light as feather...and something in the back of your brain knew it was true.\nDespite the unusual circumstances, you remain calm...") 
  if input("-----------------------------------------------------------(Enter anything to continue)\n"):
    print("By making the right choices, you hope to gain access to the control room and bring the ship back home.\nYou don't know if there is anyone else in the space ship with you, so you will be stealthy. ")
    if input("-----------------------------------------------------------(Enter anything to continue)\n"):
      check_for_start("start")


# # create a variable that holds on to the correct amount of tools needed to win the game
# correctItems = 2

# # each condition where if the right items aren't chosen, you describe the reason why you need it
# if "C" not in userList:
#   print("You need batteries to start up something\n")
# if "D" not in userList:
#   print("You need a tool to see at night\n")

# # condition where you will the right choices were there BUT there are other options that were chosen
# if "C" and "D" in userList:
#   print("You have chosen the right tools to get out of the woods BUT too many items! \n")
#   # nested condition where you will win the game if you have the right tools 
#   if len(userList) == correctItems:
#     print("You have chosen the right tools to get out of the woods! \n")
#     print("======= YOU WON =======")
# else:
#   print("You have chosen the wrong tools to get out of the woods, try again! \n")
