import os, time

oxygen = False
submarine = False
map = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Hi! You are the Tim the Giraffe and you are going to explore the ocean.")
  print()
  print()
  print("Let's get started!")
  time.sleep(5) # wait 3 seconds before moving on
  cave1() # runs to send the player to cave #1

def cave1():
  global submarine # use the submarine variable from the top
  os.system('clear')
  if submarine:
    print("You have a submarine!  You can start exploring!")
    print("Type the word two")
  else:
    print("Which mode of transportation do you chose for your underwater exploration? A submarine, a car, or a kayak?")
  decision = input(">>").strip().lower()
  if decision.find("submarine") > -1:
    print("Good choice!")
    submarine = True
    time.sleep(3)
    cave1()
  elif decision.find("car") > -1:
    print("Are you kidding.  That's a terrible idea.")
    time.sleep(3)
    cave1()
  elif decision.find("kayak") > -1:
    print("Um, no.  That won't be able to go underwater.")
    time.sleep(3)
    cave1()
  elif decision.find("two") > -1:
    print("two")
    time.sleep(3)
    cave2()
  else:
    print("Sorry, that wasn't an option.")
    time.sleep(3)
    cave1()
  
##### over here 
def cave2():
  global map, oxygen
  os.system('clear')
  print("Welcome to Cave 2")
  if map:
    print("You have a map! Now you can choose which route to take.  The map is labeled by color.  Would you like to take the green or blue route?")
  else:
    print("You'll need a way of navigating the ocean.  You have a choice of a GPS, a map, or compass.")
  decision = input(">>").strip().lower()
  if decision.find("map") > -1:
    print("Good idea!")
    map = True
    time.sleep(3)
    cave2()
  elif decision.find("compass") > -1:
    print("I don't think this will provide enough guidance.")
    time.sleep(3)
    cave2()
  elif decision.find("GPS") > -1:
    print("That won't work underwater.")
    time.sleep(3)
    cave2()
  elif decision.find("blue") > -1:
    print("You chose Route Blue.")
    time.sleep(3)
    caveblue()
  elif decision.find("green") > -1:
    print("You chose Route Green!  Unfortunately, just as you decided which path to take, you map tore down the middle.  Lucky for you, there seems to be help ahead.")
    time.sleep(3)
    cavegreen()
  else:
    print("Try again.")
    time.sleep(3)
    cave2()

def caveblue():
  global map, oxygen
  os.system('clear')
  pass
  print("If you look to your left, you will see a family of dolphins!  It looks like they are guarding something. ")
  if oxygen:
    print("You start swimming out to the dolphins.  Do you provoke them or try to start a conversation?")
  else:
    print("You won't be able to hold your breathe for long.  Lets look around the submarine to see if there is anything that might help.")
    time.sleep(2)
    print("Ok, you found an snorkel, an oxegyn mask, and clothespin.")
  decision = input(">>").strip().lower()
  if decision.find("oxygen") > -1:
    print("Good choice.")
    oxygen = True
    time.sleep(3)
    caveblue()
  elif decision.find("snorkel") > -1:
    print("This would work if we weren't so far underwater.  Try again.")
    time.sleep(3)
    caveblue()
  elif decision.find("clothespin") > -1:
    print("This might help you hold your breath, but it won't allow you to stay underwater for long..")
    time.sleep(3)
    caveblue()
  elif decision.find("provoke") > -1:
    print("Game Over:  The dolphins attacked.")
    time.sleep(3)
    startGame()
  elif decision.find("conversation") > -1:
    print("Good choice.  The dolphins said they were hiding a secret map that they can't give away. But, they told you that they could show you the way instead.")
    time.sleep(5)
    cavegreen()
  else:
    print("Try again.")
    time.sleep(3)
    caveblue()
## over here
    
    
def cavegreen():
  global map, oxygen, kind
  os.system('clear')
  pass
  print("You are on your way!  A dolphin named Blue has decided to leave his pod and help you find your way.")
  time.sleep(2)
  print("Blue says:'Our family knows of two ocean secrets.  Would you like to discover option one or two?'")
  decision = input(">>").strip().lower()
  if decision.find("one") > -1:
    print("Blue says: The Hidden City.  I know the way, follow me!")
    map = True
    time.sleep(3)
    secret1()
  elif decision.find("two") > -1:
    print("Blue says: Hm, the Secret Treasure.  I'll need some help with this one, follow me.")
    time.sleep(3)
    secret2()
  else:
    print("That wasn't an option")
    time.sleep(3)
    cavegreen()
  

  
def secret1():
  global map, oxygen
  os.system('clear')
  pass
  print("Blue says, 'Welcome to The Hidden City.  On your left is the Humback Whale Hotel.")
  time.sleep(3)
  print("Blue says, 'Then, over there, is the Killer Whale Commons, we should probably stay away from there...'")
  print("Blue says:'Well, we have reached the end of your journey. I'm going back to my pod.  Do you want to stay here or go to the Secret Treasure?'")
  decision = input(">>").strip().lower()
  if decision.find("stay") > -1:
    print("See you later!")
    map = True
    time.sleep(3)
    startGame()
  elif decision.find("treasure") > -1:
    print("Blue says: Hm, the Secret Treasure.  I'll need some help with this one, follow me.")
    time.sleep(3)
    secret2()
  else:
    print("That wasn't an option")
    time.sleep(3)
    cavegreen()

def secret2():
  global map, oxygen
  os.system('clear')
  pass
  print("Blue is joined by his friend Dory.  They take you to the Secret Treasure.  Unusually enough, it is a box clearly labeled Secret Treasure.  However, the key was lost years ago, so there is no way to know what is inside.")
  time.sleep(3)
  print("Blue says:'Well, we have reached the end of your journey. I'm going back to my pod.  Do you want to stay here or go to the Hidden City?'")
  decision = input(">>").strip().lower()
  if decision.find("stay") > -1:
    print("See you later!")
    map = True
    time.sleep(3)
    startGame()
  elif decision.find("city") > -1:
    print("Blue says: Follow me.")
    time.sleep(3)
    secret1()
  else:
    print("That wasn't an option")
    time.sleep(3)
    cavegreen()

    
def endGame():
  os.system("clear")
  pass

startGame()