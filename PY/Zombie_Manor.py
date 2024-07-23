input_msg ="" #an empty string to hold our user inputs
game_is_on = True #the game loop will depend on this being true
current_room = None #to keep track of where we are
rooms = [] #append any new rooms you create to this list

#******** DEFINE CLASSES *******************
class Room:
    def __init__(self, name=(""), description=(""), examines=[], paths=[]):
        self.name = name
        self.description = description
        self.examines = examines #objects in the room that can be examined further
        self.paths = paths #available rooms that can be moved to

class Player:
  def __init__(self, name=None, items=[], weapons=[], wounded=False):
      self.name = name
      self.items = items
      self.weapons = weapons
      self.wounded = wounded
    
class Zombie:
   def __init__(self, description=None, spoils=[], location=None, defeated=False):
      self.description = description
      self.spoils = spoils
      self.location = location
      self.defeated = defeated

 #**********INSTANTIATE OBJECTS ***************
player = Player()
#add the rooms to the rooms list
rooms.append(workshop)
rooms.append(conservatory)
rooms.append(fountain)
rooms.append(flowerbeds)
rooms.append(shed)
rooms.append(kitchen)
rooms.append(bathroom)   