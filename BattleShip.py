#BattleShip
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
turn = 0
guess_row = 0
guess_col = 0

def geuss():
  print ("Turn", turn + 1)
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    turn + 1

for turn in range(6):
  if turn == 5:
    print ("Game Over")
  else:
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    guess_row -= 1
    guess_col -= 1
    geuss()
    if guess_row == ship_row and guess_col == ship_col:
      break

#Extra Credit
#You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!
#Make multiple battleships: you’ll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You’ll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
#Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
#Make your game a two-player game.
#Use functions to allow your game to have more features like rematches, statistics and more!
#Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!