# my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# # Remove the item with the key "age"
# del my_dict["age"]

# print(my_dict)  # Output: {"name": "Alice", "city": "New York"}



# number = 3.1

# formatted_number = "{:.2f}".format(number)  # .2f specifies 2 decimal places

# print(formatted_number)  # Output: 3.14

def prompt_user():
  reply = input("What do you want to do?  >>  ")

  return reply
prompt_user()
# coded_message = "apples are or oranges"

# coded_message.replace(coded_message(coded_message.find("or")), "to")

print("you see a work table, and behind it specimen in a giant test tube. on the worktable is a ")


("on three pedestals closest to you lay piles of three metals, x, y, and z; in the center of the room is a  sconce, lit by a blazing fire.")
hint: "You wonder what would happen if you threw the metals into the fires

"You pick up an old traveler's workbook -- on the third page, there are three circles, shaded with color ink in the following order: red, blue, green"




























#------------------------------------------------------
class Room:
  def __init__(self, name, description, objects, paths):
      self.name = name
      self.description = description
      self.objects = objects
      self.paths = paths

class Player:
  def __init__(self):
      self.name = None
      self.items = []

import sys
import readline

inputMsg = ""
gameIsOn = True
currentRoom = None
rooms = []
tries = 0

# ********** DEFINE CLASSES ***************
# class Room:
#     def __init__(self, name, description, objects, paths):
#         self.name = name
#         self.description = description
#         self.objects = objects
#         self.paths = paths

# class Player:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items


# ********** INSTANTIATE OBJECTS ***************
player = Player()

center = Room("center", "\n\n You are in the center of the room you can move to any other side of the room from here. There's also a lock.\n\n", ["rope"], ["north", "east", "west", "south", "center"])

east = Room("east", "\n\nWow this side of the room has a creepy aura. You notice an alter but it seems to be missing something in the candle slot.\n\n ", ["alter"], ["north", "south", "center", "west"])

west = Room("west", "\n\nThis seems to be the west side of the room. You notice a grate, maybe this is where the water will come from if I dont get out of here in time. There also looks like theres something something shinny in it, maybe I can pull it open with something.\n\n", ["shinny_object"], ["north", "south", "center", "east"])

north = Room("north", "\n\nThe north seems pretty bare. It just has the TV you heard the msg from. The TV is on stand thats locked. Might need a key.\n\n", [""], ["west", "east", "center", "south"])

south = Room("south", "\n\nBruh, its just a blank wall. I'm not sure what to do with this.\n\n", [""], ["west", "east", "center"])

rooms.extend([north, south, east, west, center])  # add the rooms to the rooms array


# ********** START GAME ***************
def start():
  print("\n\nYou wake up in a room and notice a tv in front of you flickering. As you wake up the tv plays a msg telling you that you have an hour to escape this room before the room will fill with water and you'll drown.There's also a code pad in the floor. \n\n\n\n\n")
  name = input("\n\nTell me your name so I can add it to my book of victims  ")
  player.name = name
  print(f"\n\n\nWell it's a shame {name} , you won't make it out of here\n\n")
  global currentRoom
  currentRoom = center
  print(f"\n\nYou are starting in the {currentRoom.name} of the room \n\n\n ")

  while gameIsOn:
      checkAnswer(promptUser())


def promptUser():
  return input("What do you want to do?\n\n ")


def checkAnswer(inputMsg):
  global gameIsOn, tries, currentRoom

  # MOVE
  if "move" in inputMsg:
      msgArray = inputMsg.split(" ")
      newRoom = msgArray[1]  # get the second element
      newRoomIndex = next((i for i, room in enumerate(rooms) if room.name == newRoom), -1)
      if currentRoom.paths.count(newRoom) > 0 and newRoomIndex != -1:
          currentRoom = rooms[newRoomIndex]
          player.currentRoom = currentRoom
          print(currentRoom.description)

  # LOOK
  elif "look" in inputMsg:
      print("You see the following: ")
      for obj in currentRoom.objects:
          print(f"- {obj}")
      print("From here you can go to: ")
      for path in currentRoom.paths:
          print(f"- {path}")
      print("------------------------------\n\n")

  # USE
  elif "use" in inputMsg:
      usedItem = inputMsg.split(" ")[1]
      if (usedItem in player.items and usedItem == 'rope') and player.currentRoom == west:
          print('\n\nYou wrap the rope around the grate and pull it off to reveal the object behind. Looks like a key\n\n')
          west.objects.remove('rope')
          west.objects.append('key')
          west.description = "\n\nThis is the west side of the room. The grate is now removed. hole behind no longer glimmers because you took the key\n\n."

      elif (usedItem in player.items and usedItem == 'key') and player.currentRoom == north:
          print(f"\n\nUsed the key to unlock the cabinent under the tv. Within the cabinent you notice a used candle.\n\n")
          north.objects.append('candle')
          north.description = "\n\nThe north still seems bare. Now the tv cabinent is open with nothing inside.\n\n "

      elif (usedItem in player.items and usedItem == 'candle') and player.currentRoom == east:
          print('\n\nYou place the candle on alter and it proceeds to glow. From the alter, a flashlight falls. I wonder what this can be used for.\n\n')
          east.objects.append('flashlight')
          east.description = "\n\nThe east's alter now glows from the candle.\n\n "

      elif (usedItem in player.items and usedItem == 'flashlight'):
          if currentRoom != south:
              print(f"\n\nturns on but its just purple... is it a UV light?\n\n")
          else:
              print(f"\n\nYou shine the light on the seemingly blank wall to reveal a writing on the wall 'c0d3n3xt'\n\n")
              center.objects.append('codelock')

      elif usedItem == 'codelock' and player.currentRoom == center:
          userCode = input("enter code.... ")
          if userCode == 'c0d3n3xt':
              print(f"\n\nThe lock unlocks and the room opens of as if you are in a tv studio. An individual walks towards you with a smile on their face. They shake your hand to congratulate you on escaping the room and hand you a giant check for a bazillion dollars. The TV studio fills with applause. You are immensely confused but at least you are no longer trapped in a room and are a baziliion dollars richer.\n\n")
              gameIsOn = False
          elif userCode != 'c0d3n3xt':
              tries += 1
              print(f"\n\nwrong you have guessed {tries} times\n\n")
              if tries == 3:
                  print(f" you have guessed three too many times. Water begins to fill the room and you begin to panic. This looks like it's the end. Just as the water reaches your ankles, the room opens up as if you are in a tv studio. An individual walks towards you solemnly. As the water spills out of the set, the crowd claps and you're told that you were on a game show called 'Escape room'. Despite the explaination you are imensely confused. You are walked off set and the show host gives closing remarks. game over?\n\n ")
                  gameIsOn = False
              else:
                  pass
          else:
              print(f"you died")

      else:
          print('does not look like that will work here')

  # TAKE
  elif "take" in inputMsg:
      itemToTake = inputMsg.split(" ")[1]
      if itemToTake in currentRoom.objects:
          print(f"Yes you can take this item: {itemToTake}")
          player.items.append(itemToTake)
          currentRoom.objects.remove(itemToTake)
      else:
          print("No you can't pick that up")

  # WHERE
  elif "where" in inputMsg:
      print(currentRoom.name)

  # HELP
  elif "help" in inputMsg:
      print("\n\nType 'look' to look around and see objects in the environment along with the paths you can go.\n\nType 'move' followed by where you want to go to move around the room.\n\nType 'use' followed by what you want to use to use the object.\n\nType 'take' followed by the object you wanted to take \n\nType 'where' to get a reminder of where you are.\n\nType 'inventory' to see what's in your inventory.\n\n")

  # INVENTORY
  elif inputMsg == "inventory":
      print(player.items)

  # I DON'T UNDERSTAND
  else:
      print(" I don't understand that")


start()
