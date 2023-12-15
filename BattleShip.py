#BattleShip
import os
from random import randint
import time

os.system('cls')

if(not os.path.isfile("./settings.txt")):
  filesettings = open("settings.txt", "xt")

  filesettings.write("3\n")
  filesettings.write("15\n")
  filesettings.write("5\n")
  filesettings.write("5\n")

  filesettings.close()

filesettings = open("settings.txt", "r")

settings = filesettings.readlines()

battleShips = (int)(settings[0].replace("n","").replace('\\',""))

guesses = 1 + (int)(settings[1].replace("n","").replace('\\',""))
numRows = (int)(settings[2].replace("n","").replace('\\',""))
numCols = (int)(settings[3].replace("n","").replace('\\',""))

filesettings.close()

ship_row = 0
ship_col = 0

board = []
battleShipsPosition = []

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

#Append the amount squares that thier are collums to the amount of rows to the board
def setBoard():
  board = []
  for x in range(numRows):
    board.append(["[ ]"] * numCols)
  return board

def print_board(theboard):
  for row in theboard:
    for col in range(numCols):
      print(row[col], end="")
    print(end="\n")

#Define random_row and random_col to return random number within the length of the board
def random_row():
  return randint(0, numRows-1)

def random_col():
  return randint(0, numCols-1)

def positionShips():
  battleShipsPosition = []
  firstTime = True
  ship_row = random_row()
  ship_col = random_col()
  ships = []
  for ship in range(battleShips):
    ships.append(ship)
    while True:
      ship_row = random_row()
      ship_col = random_col()
      if firstTime:
        battleShipsPosition.append([random_row(), random_col()])
        firstTime = False
        break
      occupied = False
      for boat in range(len(battleShipsPosition)):
        if ship_row == battleShipsPosition[boat][0] and ship_col == battleShipsPosition[boat][1]:
          occupied = True
      if occupied == True:
        continue
      else:
        battleShipsPosition.append([ship_row, ship_col])
        break
  return battleShipsPosition

#positionShips()

#ship_row = random_row(board)
#ship_col = random_col(board)

def game():

  #initial setup
  turn = 0
  guess_row = 0
  guess_col = 0

  won = False

  board = setBoard()
  battleShipsPosition = positionShips()

  #Intro Statement
  print("Welcome to Battleship! You need to guess the locations of " + (str)(battleShips) + " hidden battleships!")

  print_board(board)

  print("Type \"exit\" if you would like to quit")

  won = False
  shipsSunk = 0
  playerTimeTurn = 1

  while playerTimeTurn != guesses:
    if won != True:   
      notInOcean = False
      won = False

      exited = False

      while True:
        try:
          guess_row = input("Guess Row: ")
          if(guess_row == "exit" or guess_row == "Exit"):
            exited = True
            break
          else:
            guess_row = (int)(guess_row)
          guess_col = input("Guess Collumn: ")
          if(guess_col == "exit" or guess_col == "Exit"):
            exited = True
            break
          else:
            guess_col= (int)(guess_col)
        except:
          os.system('cls')
          print("Turn " + str(playerTimeTurn))
          print_board(board)
          print("Try Again, Invalid Answer")
        else:
          break
      if exited:
        break

      guess_row -= 1
      guess_col -= 1

      if (guess_row < 0 or guess_row > numRows-1) or (guess_col < 0 or guess_col > numCols-1):
        os.system('cls')
        print ("Turn", playerTimeTurn)
        print_board(board)
        print ("Oops, that's not even in the ocean.")
        notInOcean = True
      elif (board[guess_row][guess_col] == "[O]" or board[guess_row][guess_col] == "[X]"):
        os.system('cls')
        print ("Turn", playerTimeTurn)
        print_board(board)
        print ("You guessed that one already.")
      for ship in range(battleShips):
        if guess_row == battleShipsPosition[ship][0] and guess_col == battleShipsPosition[ship][1] and board[guess_row][guess_col] != "[X]":
          board[guess_row][guess_col] = "[X]"
          os.system('cls')
          playerTimeTurn += 1
          print ("Turn", playerTimeTurn)
          print_board(board)
          shipsSunk += 1
          if shipsSunk == battleShips:
            won = True
            print("Congratulations! You sunk all of my battleship!")
            break
          else:
            print("Congratulations! You sunk one of my battleship! You still need to sink: " + (str)(battleShips-shipsSunk))
            break
        else:
          continue

      if won == False and notInOcean == False and board[guess_row][guess_col] == "[ ]":
        os.system('cls')
        playerTimeTurn += 1
        print ("Turn", playerTimeTurn)
        board[guess_row][guess_col] = "[O]"
        print_board(board)
        print ("You missed my battleship!")
      #print_board(board)
      notInOcean = False
      if won == True:
        print("You Won in " + str(playerTimeTurn) + " turns!")
        break
      print("You have " + str(guesses-playerTimeTurn) + " turns left")
  if exited:
    return 0
  else:
    print ("Game Over")
    time.sleep(5)
    mode = False

mode = False

while(mode == False):
  os.system('cls')
  print("1. Play BattleShip")
  print("2. Settings")
  print("3. Exit Game")
  while True:
    try:
      inputMode = input("Enter the mode: ")
    except:
      os.system('cls')
      print("Try Again, Invalid Answer")
      time.sleep(1)
    else:
      break
  if inputMode == "1":
    mode = True
    os.system('cls')
    setBoard()
    positionShips()
    game()
    mode = False
  elif inputMode == "2":
    os.system('cls')

    numOfBattleShips = input("Enter the number of battleships you would like: ")
    numOfGuesses = input("Enter the number of guesses you would like: ")
    numOfRows = input("Enter the number of rows you would like: ")
    numOfCollumns = input("Enter the number of collumns you would like: ")

    os.remove("settings.txt")

    filesettings = open("settings.txt", "xt")
    filesettings.close()
    filesettings = open("settings.txt", "w")
    try:
      filesettings.write(numOfBattleShips + "\n")
      filesettings.write(numOfGuesses + "\n")
      filesettings.write(numOfRows + "\n")
      filesettings.write(numOfCollumns + "\n")

      filesettings.close()

      filesettings = open("settings.txt", "r")
      settings =  filesettings.readlines()

      battleShips = (int)(settings[0])
      guesses = 1 + (int)(settings[1].replace("n","").replace('\\',""))
      numRows = (int)(settings[2].replace("n","").replace('\\',""))
      numCols = (int)(settings[3].replace("n","").replace('\\',""))
    finally:
      filesettings.close()

    time.sleep(1)
    mode == False
  elif inputMode == "3":
    exit()
  else:
    print("Try Again, Invalid Answer")
    time.sleep(1)
    mode == False




#Extra Credit
#You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!
#Make multiple battleships: you’ll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You’ll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
#Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
#Make your game a two-player game.
#Use functions to allow your game to have more features like rematches, statistics and more!
#Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!1