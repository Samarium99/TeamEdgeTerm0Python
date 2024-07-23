input_msg ="" #an empty string to hold our user inputs
game_is_on = True #the game loop will depend on this being true
current_room = None #to keep track of where we are
rooms = [] #append any new rooms you create to this list
day = 1
time = "day"
numMoves = 0

#******** DEFINE CLASSES *******************
class Room:
  def __init__(self, name=None, description=None, objects=None, paths=None):
    self.name = name
    self.description = description
    self.objects = objects
    self.paths = paths
      
class Player:
  def __init__(self, name=None, items=[]):
      self.name =name
      self.items = items

class Zombie:
   def __init__(self, description=None, spoils=[], location=None):
      self.description = description
      self.spoils = spoils
      self.location = location
#**********INSTANTIATE OBJECTS ***************
player = Player()

workshop = Room()
workshop.name = "Workshop"
workshop.description = "You slide down the ladder for what feels like exactly 5 minutes and 9 seconds.\nYou know that because you counted.\n\n Stepping off of the ladder, you are in a dimly lit room with stone walls. There is a cauldron in the far corner, bubbling some sort of"
workshop.objects =[" "]
workshop.paths=["Conservatory"]

conservatory = Room()
conservatory.name = "Conservatory"
conservatory.description = "The conservatory is breathtaking, or you assume that it was at some point.\nOvergrown vines suffocate the glass walls, only allowing small fragments of light to enter. \nYou notice a small, cracked fountain that sits at the center, with several flowerbeds circling around it, not much different from the one you awoke from. \nSquinting across the conservatory, you see a humble shed hidden in a nook."
conservatory.objects =[" "]
conservatory.paths=["Fountain", "Flowerbeds", "Shed","L2 Corridor"]

fountain = Room()
fountain.name = "Fountain"
fountain.description = "The fountain no longer runs, however, it is filled with a swirling, murky liquid, clouding most sight of the bottom.\nAt the edge of the fountain, there is a rusty pipe, perhaps from an failed attempt to repair the structure."
fountain.objects =["pipe"]
fountain.paths= ["Flowerbeds", "Shed","L2 Corridor"]

flowerbeds = Room()
flowerbeds.name = "Flowerbeds"
flowerbeds.description = "You walk along the flowerbeds, scanning for any abnormalities. Suddenly, a flacid and discolored hand shoots up, grabbing for your ankle >:3"
flowerbeds.objects =[" "]
flowerbeds.paths= ["Fountain", "Flowerbeds", "Shed","L2 Corridor"]

shed = Room()
shed.name = "Shed"
shed.description = "The wooden toolshed is shabby at best, made of a rotting wood. Opening its doors, you can't help but note the lack of equipment...instead, there is a hole in the shed's floor, filled with a ladder leading into darkness...what??"
shed.objects =[" "]
shed.paths= ["Fountain", "Shed", "L2 Corridor"]

flowerdemon = Zombie()
flowerdemon.description = ("This zombie suddenly attacked from under the cover of withered flowers. It has flowers stuck in its long, matted locks. The zombie holds no weapons.")
flowerdemon.spoils = (" ")
flowerdemon.location = ("Flowerbeds", "Conservatory")

kitchen = Room()
kitchen.name = "Kitchen"
kitchen.description = "The kitchen is a really nice one! It has all the stuff you need to cook a healthy meal...of zombie parts! On the table there is a red pill."
kitchen.objects =["potion", "sandwich", "knife"]
kitchen.paths=["Livingroom" , "Bathroom" , "Backyard" ]

bathroom = Room() 
bathroom.name= "Bathroom"
bathroom.description ="You are in a Bathroom. Everything is a mess. There is blood on the floor. The shower is still on... "
bathroom.objects = ["towel" , "toothbrush", "toilet Paper", "soap"]
bathroom.paths =["Kitchen"]

#add the rooms to the rooms list
rooms.append(workshop)
rooms.append(conservatory)
rooms.append(fountain)
rooms.append(flowerbeds)
rooms.append(shed)
rooms.append(kitchen)
rooms.append(bathroom)


def day_night_cycle():
   global numMoves
   if time == "day" and numMoves == 10:
        time = "night"
        print(f"NIGHT of DAY {day}")
        numMoves = 0
   elif time == "night" and numMoves == 10:
        time = "day"
        day += 1
        print(f"MORNING of DAY {day}")




   
def prompt_user():
  reply = input("\nWhat do you want to do?  >>  ")
  return reply

def check_answer(input):
  global current_room
  global input_msg
  global rooms

  print("\nchecking input:  " +  input)
  input_msg = input

  #GO
  if "go" in input_msg:

    #split the string into two arguments
    msg_array  = input_msg.split(" ")
    new_room = msg_array[1].title() #get the second element
    print(" user typed go to " + new_room)

    if new_room in current_room.paths:
       global numMoves
       print("Yes you can go there")
       #find the room that has that "key" new_room as a property
       for room in rooms:  #Make challenge!!!!
          if room.name.lower() == new_room.lower():
            #set the current room by grabbing its index
            index = rooms.index(room)
            current_room = rooms[index]
            print("You are now at the : " + current_room.name + "\n\n" + current_room.description)
            numMoves += 1
    else:
        print("No you can't go there")
      
  #LOOK          
  elif "look" in input_msg:
      #loop through all the objects and paths and print them out so user can see options
      print("You can pick up the following: ") 
      for object in current_room.objects:
          print(" -  " + object)
      print("From here you can go to: ")
      for path in current_room.paths:
          print(" - " + path)
        #   numMoves += 1
  #TAKE
  elif "take" in input_msg:
      print("Taking item...")

      items_list  = input_msg.split(" ")
      item_to_take = items_list[1] #get the second element

      #check to see if it is part of the room's inventory..

      if item_to_take in current_room.objects:
          print("Yes you can take this item: " + item_to_take)
          player.items.append(item_to_take) #add to the players items list

          #remove from room
          current_room.objects.remove(item_to_take)

          print("current room items after taking item " + str(current_room.objects))
          print("player has : " + str(player.items))
          numMoves += 1
      else:
          print("No you can't pick that up")
#   elif "attack" in input_msg:
#       if "pipe" in player.items:
#         if
#         else:
#         print("You cannot use this item at the moment.")
#       else:
#       print: ("You do not have a weapon")

  #USE

  #Name
  elif "name" in input_msg:
      print( current_room.name)

  #Help
  elif "help" in input_msg:
      print("Type:\n 'look' to look around\n 'go ____' to follow a path\n 'take ____' to pick up an item\n 'help' to receive this information")
      
  elif input_msg == None:
      print(" input: " + input_msg)
        
      input_msg = input("What do you want to do? You can type 'help' for commands to use >>> ")
      
  else:
      print(" I don't understand that")

def coffin_death():
   global coffin
   global game_is_on
   coffin = input(str("WHERE ARE YOU?!\n A "))
   death_near = 0
   if coffin.strip().lower() == "coffin":
        print(f"That sounds about right! You push as hard as you can against the lid, somehow letting yourself out of death's grasp.\nBrushing the dirt off of your clothes, you wonder where you are...\nIt seems like you are in a: {current_room.name}.")
   else:
        print("That's wrong, try again!\nHint: You are in the dark, and you smell dirt, death, and wood.")
        death_near += 1
       
        if death_near >= 4:
            print("\n\nYou run out of air and suffocate to death...R.I.P.")
            game_is_on = False
        else:
           return coffin_death()

def start():
  global current_room

  print("This is Untitled Game")
  name = input("What is your name, player?\n")
  player.name = name
  print("Welcome, " + name)

  #begin at the conservatory
  current_room = conservatory
  print(f"\nYou wake up, staring up into darkness.\nYou breath in the stench of death and dirt and wood...and start to panic...you start to feel lightheaded...")
  
  coffin_death()
  print(f"\n----- MORNING of DAY {day} ----- \n\nType:\n 'look' to look around\n 'go ____' to follow a path\n 'take ____' to pick up an item\n 'help' to receive this information")


#--------------------------------------------------------------------------#
start()
while(game_is_on):
    check_answer(prompt_user()) #this makes the game continously prompt and check response