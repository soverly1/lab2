import xml.etree.ElementTree as ET
""" Imports the xml module 
for use throughout the program"""
global player
global inventory
global item
global mob
global wall
global command

class World:
  def __init__(self, node):
    self.cave={}
    self.location=""
    for child in node:
      if child.tag=="cave":
        genCave=Cave(child)
        self.cave[genCave.title]=genCave
        self.location==""
        self.location=genCave.title

class Wall:
  def __init__(self,node):
    self.direction=node.find("direction").text
    self.title=node.find("title").text
    self.command=node.find("command").text

class Cave:
  def __init__(self,node):
    self.title=node.find("title").text
    self.description=node.find("description").text
    self.items=[]
    for o in node.findall("./item"):
      self.items.append(o.text)
      #print(self.items)
    self.walls=[]
    for i in node.findall("./wall"):
      w=Wall(i)
      self.walls.append(i)
      #print(self.walls)
     #print(self.walls)

  def describe(self):
    print(self.title)
    print(self.description)
    for i in self.items:
      things=[]
      things.append(i)
      print(things)
    for a in things:
      print(a)

  def checkForWalls(self,user_command):
    for w in self.walls:
      #print(self.walls)
      #print(w)
      if self.command==user_command:
        return w.title
        print(w.title)
      else:
        return None

def generateWorld():
  global cave
  global location
  tree = ET.parse('game.xml')
  root = tree.getroot()
  world=World(root)
  return world

def processCommand(newworld):
  try:
    c=str(input(">"))
    moveCave=newworld.cave[newworld.location].checkForWalls(c)
    if (moveCave!=None):
      world.location=moveCave
    else:
      print("There's a wall here! Try going in another direction...") 
  except TypeError:
    print("Cannot read numeric commands!") 

def runGame(newworld):
  while True:
    newworld.cave[newworld.location].describe()
    processCommand(newworld)

newworld=generateWorld()
runGame(newworld)

  



