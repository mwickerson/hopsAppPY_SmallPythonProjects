"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

#Small Python Projects

# """
# ███╗   ███╗ █████╗ ███████╗███████╗
# ████╗ ████║██╔══██╗╚══███╔╝██╔════╝
# ██╔████╔██║███████║  ███╔╝ █████╗  
# ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  
# ██║ ╚═╝ ██║██║  ██║███████╗███████╗
# ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
# """
# #write a walker algorithm to build a 3D labyrinth
# # df_maze.py
# import random

# # Create a maze using the depth-first algorithm described at
# # https://scipython.com/blog/making-a-maze/
# # Christian Hill, April 2017.

# class Cell:
#     """A cell in the maze.

#     A maze "Cell" is a point in the grid which may be surrounded by walls to
#     the north, east, south or west.

#     """

#     # A wall separates a pair of cells in the N-S or W-E directions.
#     wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

#     def __init__(self, x, y):
#         """Initialize the cell at (x,y). At first it is surrounded by walls."""

#         self.x, self.y = x, y
#         self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

#     def has_all_walls(self):
#         """Does this cell still have all its walls?"""

#         return all(self.walls.values())

#     def knock_down_wall(self, other, wall):
#         """Knock down the wall between cells self and other."""

#         self.walls[wall] = False
#         other.walls[Cell.wall_pairs[wall]] = False


# class Maze:
#     """A Maze, represented as a grid of cells."""

#     def __init__(self, nx, ny, ix=0, iy=0):
#         """Initialize the maze grid.
#         The maze consists of nx x ny cells and will be constructed starting
#         at the cell indexed at (ix, iy).

#         """

#         self.nx, self.ny = nx, ny
#         self.ix, self.iy = ix, iy
#         self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

#     def cell_at(self, x, y):
#         """Return the Cell object at (x,y)."""

#         return self.maze_map[x][y]

#     def __str__(self):
#         """Return a (crude) string representation of the maze."""

#         maze_rows = ['-' * self.nx * 2]
#         for y in range(self.ny):
#             maze_row = ['|']
#             for x in range(self.nx):
#                 if self.maze_map[x][y].walls['E']:
#                     maze_row.append(' |')
#                 else:
#                     maze_row.append('  ')
#             maze_rows.append(''.join(maze_row))
#             maze_row = ['|']
#             for x in range(self.nx):
#                 if self.maze_map[x][y].walls['S']:
#                     maze_row.append('-+')
#                 else:
#                     maze_row.append(' +')
#             maze_rows.append(''.join(maze_row))
#         return '\n'.join(maze_rows)

#     def write_svg(self, filename):
#         """Write an SVG image of the maze to filename."""

#         aspect_ratio = self.nx / self.ny
#         # Pad the maze all around by this amount.
#         padding = 10
#         # Height and width of the maze image (excluding padding), in pixels
#         height = 500
#         width = int(height * aspect_ratio)
#         # Scaling factors mapping maze coordinates to image coordinates
#         scy, scx = height / self.ny, width / self.nx

#         def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
#             """Write a single wall to the SVG image file handle f."""

#             print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
#                   .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

#         # Write the SVG image file for maze
#         with open(filename, 'w') as f:
#             # SVG preamble and styles.
#             print('<?xml version="1.0" encoding="utf-8"?>', file=f)
#             print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
#             print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
#             print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
#                   .format(width + 2 * padding, height + 2 * padding,
#                           -padding, -padding, width + 2 * padding, height + 2 * padding),
#                   file=f)
#             print('<defs>\n<style type="text/css"><![CDATA[', file=f)
#             print('line {', file=f)
#             print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
#             print('    stroke-width: 5;\n}', file=f)
#             print(']]></style>\n</defs>', file=f)
#             # Draw the "South" and "East" walls of each cell, if present (these
#             # are the "North" and "West" walls of a neighbouring cell in
#             # general, of course).
#             for x in range(self.nx):
#                 for y in range(self.ny):
#                     if self.cell_at(x, y).walls['S']:
#                         x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
#                         write_wall(f, x1, y1, x2, y2)
#                     if self.cell_at(x, y).walls['E']:
#                         x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
#                         write_wall(f, x1, y1, x2, y2)
#             # Draw the North and West maze border, which won't have been drawn
#             # by the procedure above.
#             print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
#             print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
#             print('</svg>', file=f)

#     def find_valid_neighbours(self, cell):
#         """Return a list of unvisited neighbours to cell."""

#         delta = [('W', (-1, 0)),
#                  ('E', (1, 0)),
#                  ('S', (0, 1)),
#                  ('N', (0, -1))]
#         neighbours = []
#         for direction, (dx, dy) in delta:
#             x2, y2 = cell.x + dx, cell.y + dy
#             if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
#                 neighbour = self.cell_at(x2, y2)
#                 if neighbour.has_all_walls():
#                     neighbours.append((direction, neighbour))
#         return neighbours

#     def make_maze(self):
#         # Total number of cells.
#         n = self.nx * self.ny
#         cell_stack = []
#         current_cell = self.cell_at(self.ix, self.iy)
#         # Total number of visited cells during maze construction.
#         nv = 1

#         while nv < n:
#             neighbours = self.find_valid_neighbours(current_cell)

#             if not neighbours:
#                 # We've reached a dead end: backtrack.
#                 current_cell = cell_stack.pop()
#                 continue

#             # Choose a random neighbouring cell and move to it.
#             direction, next_cell = random.choice(neighbours)
#             current_cell.knock_down_wall(next_cell, direction)
#             cell_stack.append(current_cell)
#             current_cell = next_cell
#             nv += 1

# #write into a @hops component
# @hops.component(
#     "/Maze_07",
#     name="Maze_01",
#     description="Maze_01",
#     inputs=[
#         hs.HopsInteger("nx", "nx", "nx", access = hs.HopsParamAccess.ITEM),
#         hs.HopsInteger("ny", "ny", "ny", access = hs.HopsParamAccess.ITEM),
#         hs.HopsInteger("ix", "ix", "ix", access = hs.HopsParamAccess.ITEM),
#         hs.HopsInteger("iy", "iy", "iy", access = hs.HopsParamAccess.ITEM)
#     ],
#     outputs=[
#         hs.HopsString("Maze", "Maze", "Maze", access = hs.HopsParamAccess.ITEM)
#     ],
# )
# def Maze_07(nx: int, ny: int, ix: int, iy: int):
#     # Create a maze and write it to a SVG file.
#     maze = Maze(nx, ny, ix, iy)
#     maze.make_maze()
#     maze.write_svg('maze.svg')
#     return ("Congradulations, you just made a maze!")

# """
# ██████╗  █████╗  ██████╗ ███████╗██╗     ███████╗
# ██╔══██╗██╔══██╗██╔════╝ ██╔════╝██║     ██╔════╝
# ██████╔╝███████║██║  ███╗█████╗  ██║     ███████╗
# ██╔══██╗██╔══██║██║   ██║██╔══╝  ██║     ╚════██║
# ██████╔╝██║  ██║╚██████╔╝███████╗███████╗███████║
# ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
# """

# #Bagels, by Al Sweigart al@inventwithpython
# #A deductive logic game where you must guess a number based on clues
# #View this code at https://nostarch.com/big-book-small-python-projects
# #A version of this game is featured in the book "Invent Your Own
# #Computer Games with Python" https://nostarch.com/inventwithpython
# #Tags - short, game, puzzle

# import random

# NUM_DIGITS = 3 #(!) Try setting this to 1 or 10.
# MAX_GUESSES = 10 #(!) Try setting this to 1 or 100.

# def main():
#     print('''Bagels, a deductive logic game.
# By Al Sweigart al@inventwithpython

# I am thinking of a {}-digit number with no repeated digits.
# Try to guess what it is. Here are some clues:
# When I say:    That means:
#   Pico         One digit is correct but in the wrong position.
#   Fermi        One digit is correct and in the right position.
#   Bagels       No digit is correct.

# For example, if the secret number was 248 and your guess was 843, the
# clues would be Fermi Pico.'''.format(NUM_DIGITS))

#     while True: # Main game loop.
#         # This stores the secret number the player needs to guess:
#         secretNum = getSecretNum()
#         print('I have thought up a number.')
#         print('  You have {} guesses to get it.'.format(MAX_GUESSES))

#         numGuesses = 1
#         while numGuesses <= MAX_GUESSES:
#             guess = ''
#             # Keep looping until they enter a valid guess:
#             while len(guess) != NUM_DIGITS or not guess.isdecimal():
#                 print('Guess #{}: '.format(numGuesses))
#                 guess = input('> ')

#             clues = getClues(guess, secretNum)
#             print(clues)
#             numGuesses += 1

#             if guess == secretNum:
#                 # They're correct, so break out of this loop.
#                 break
#             if numGuesses > MAX_GUESSES:
#                 print('You ran out of guesses.')
#                 print('The answer was {}.'.format(secretNum))

#         # Ask player if they want to play again.
#         print('Do you want to play again? (yes or no)')
#         if not input('> ').lower().startswith('y'):
#             break
#     print('Thanks for playing!')

# def getSecretNum():
#     """Returns a string made up of NUM_DIGITS unique random digits."""
#     numbers = list('0123456789') # Create a list of digits 0 to 9.
#     random.shuffle(numbers) # Shuffle them into random order.

#     # Get the first NUM_DIGITS digits in the list for the secret number:
#     secretNum = ''
#     for i in range(NUM_DIGITS):
#         secretNum += str(numbers[i])
#     return secretNum

# def getClues(guess, secretNum):
#     """Returns a string with the pico, fermi, bagels clues for a guess
#     and secret number pair."""
#     if guess == secretNum:
#         return 'You got it!'

#     clues = []

#     for i in range(len(guess)):
#         if guess[i] == secretNum[i]:
#             # A correct digit is in the correct place.
#             clues.append('Fermi')
#         elif guess[i] in secretNum:
#             # A correct digit is in the incorrect place.
#             clues.append('Pico')
#     if len(clues) == 0:
#         return 'Bagels' # There are no correct digits at all.
#     else:
#         # Sort the clues into alphabetical order so their original order
#         # doesn't give information away.
#         clues.sort()
#         # Make a single string from the list of string clues.
#         return ' '.join(clues)

# # If the program is run (instead of imported), run the game:
# if __name__ == '__main__':

#     main()

# #write into a @hops component
# @hops.component(
#     "/Bagels_09",
#     name="Bagels_01",
#     description="Bagels_01",
#     inputs=[
#         hs.HopsInteger("NUM_DIGITS", "NUM_DIGITS", "NUM_DIGITS", access = hs.HopsParamAccess.ITEM),
#         hs.HopsInteger("MAX_GUESSES", "MAX_GUESSES", "MAX_GUESSES", access = hs.HopsParamAccess.ITEM)
#     ],
#     outputs=[
#         hs.HopsString("Have fun in the console guessing the number!", "Have fun in the console guessing the number!", "Have fun in the console guessing the number!", access = hs.HopsParamAccess.ITEM)
#     ],
# )
# def Bagels_09(NUM_DIGITS: int, MAX_GUESSES: int):
#     print('''Bagels, a deductive logic game.
# By Al Sweigart al@inventwithpython

# I am thinking of a {}-digit number with no repeated digits.
# Try to guess what it is. Here are some clues:
# When I say:    That means:
#   Pico         One digit is correct but in the wrong position.
#   Fermi        One digit is correct and in the right position.
#   Bagels       No digit is correct.

# For example, if the secret number was 248 and your guess was 843, the
# clues would be Fermi Pico.'''.format(NUM_DIGITS))

#     while True: # Main game loop.
#         # This stores the secret number the player needs to guess:
#         secretNum = getSecretNum()
#         print('I have thought up a number.')
#         print('  You have {} guesses to get it.'.format(MAX_GUESSES))

#         numGuesses = 1
#         while numGuesses <= MAX_GUESSES:
#             guess = ''
#             # Keep looping until they enter a valid guess:
#             while len(guess) != NUM_DIGITS or not guess.isdecimal():
#                 print('Guess #{}: '.format(numGuesses))
#                 guess = input('> ')

#             clues = getClues(guess, secretNum)
#             print(clues)
#             numGuesses += 1

#             if guess == secretNum:
#                 # They're correct, so break out of this loop.
#                 break
#             if numGuesses > MAX_GUESSES:
#                 print('You ran out of guesses.')
#                 print('The answer was {}.'.format(secretNum))

#         # Ask player if they want to play again.
#         print('Do you want to play again? (yes or no)')
#         if not input('> ').lower().startswith('y'):
#             break
#     return ('Thanks for playing!')

    
# def getSecretNum():
#     """Returns a string made up of NUM_DIGITS unique random digits."""
#     numbers = list('0123456789') # Create a list of digits 0 to 9.
#     random.shuffle(numbers) # Shuffle them into random order.

#     # Get the first NUM_DIGITS digits in the list for the secret number:
#     secretNum = ''
#     for i in range(NUM_DIGITS):
#         secretNum += str(numbers[i])
#     return secretNum

# def getClues(guess, secretNum):
#     """Returns a string with the pico, fermi, bagels clues for a guess
#     and secret number pair."""
#     if guess == secretNum:
#         return 'You got it!'

#     clues = []

#     for i in range(len(guess)):
#         if guess[i] == secretNum[i]:
#             # A correct digit is in the correct place.
#             clues.append('Fermi')
#         elif guess[i] in secretNum:
#             # A correct digit is in the incorrect place.
#             clues.append('Pico')
#     if len(clues) == 0:
#         return 'Bagels' # There are no correct digits at all.
#     else:
#         # Sort the clues into alphabetical order so their original order
#         # doesn't give information away.
#         clues.sort()
#         # Make a single string from the list of string clues.
#         return ' '.join(clues)

# # If the program is run (instead of imported), run the game:
# if __name__ == '__main__':
#     main()

# """
# ██████╗ ██╗██████╗ ████████╗██╗  ██╗██████╗  █████╗ ██╗   ██╗
# ██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
# ██████╔╝██║██████╔╝   ██║   ███████║██║  ██║███████║ ╚████╔╝ 
# ██╔══██╗██║██╔══██╗   ██║   ██╔══██║██║  ██║██╔══██║  ╚██╔╝  
# ██████╔╝██║██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║   ██║   
# ╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                             
# ██████╗  █████╗ ██████╗  █████╗ ██████╗  ██████╗ ██╗  ██╗    
# ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝    
# ██████╔╝███████║██████╔╝███████║██║  ██║██║   ██║ ╚███╔╝     
# ██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║  ██║██║   ██║ ██╔██╗     
# ██║     ██║  ██║██║  ██║██║  ██║██████╔╝╚██████╔╝██╔╝ ██╗    
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝ 
# """
# #The Birthday Paradox
# #https://www.youtube.com/watch?v=KtT_cgMzHx8
# """The birthday paradox says that the probability that two people in a room will have the same birthday is more than half,
# provided n, the number of people in the room, is more than 23. This property is not really a paradox, but many people find it surprising.
# Design a Python program that can test this paradox by a series of experiments on randomly generated birthdays, which test this paradox for n = 5,10,15,20, . . . ,100."""
# import random, datetime

# def getBirthdays(numberOfBirthdays):
#     """Returns a list of number random date objects for birthdays."""
#     birthdays = []
#     for i in range(numberOfBirthdays):
#         # The year is unimportant for our simulation, as long as all
#         # birthdays have the same year.
#         startOfYear = datetime.date(2001, 1, 1)

#         # Get a random day into the year:
#         randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
#         birthday = startOfYear + randomNumberOfDays
#         birthdays.append(birthday)
#     return birthdays

# def getMatch(birthdays):
#     """Returns the date object of a birthday that occurs more than once
#     in the birthdays list."""
#     if len(birthdays) == len(set(birthdays)):
#         return None # All birthdays are unique, so return None.

#     # Compare each birthday to every other birthday:
#     for a, birthdayA in enumerate(birthdays):
#         for b, birthdayB in enumerate(birthdays[a + 1 :]):
#             if birthdayA == birthdayB:
#                 return birthdayA # Return the matching birthday.

# # Display the intro:
# print('''The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
# This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.''')
# print()

# # Set up a tuple of month names in order:
# MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# while True: # Keep asking until the user enters a valid amount.
#     print('How many birthdays shall I generate? (Max 100)')
#     response = input('> ')
#     if response.isdecimal() and (0 < int(response) <= 100):
#         numBDays = int(response)
#         break
# print()

# # Generate and display the birthdays:
# print('Here are', numBDays, 'birthdays:')
# birthdays = getBirthdays(numBDays)
# for i, birthday in enumerate(birthdays):
#     if i != 0:
#         # Display a comma for each birthday after the first birthday.
#         print(', ', end='')
#     monthName = MONTHS[birthday.month - 1]
#     dateText = '{} {}'.format(monthName, birthday.day)
#     print(dateText, end='')
# print()
# print()

# # Determine if there are two birthdays that match.
# match = getMatch(birthdays)

# # Display the results:
# print('In this simulation, ', end='')
# if match != None:
#     monthName = MONTHS[match.month - 1]
#     dateText = '{} {}'.format(monthName, match.day)
#     print('multiple people have a birthday on', dateText)
# else:
#     print('there are no matching birthdays.')
# print()

# # Run through 100,000 simulations:
# print('Generating', numBDays, 'random birthdays 100,000 times...')
# input('Press Enter to begin...')
# print()

# print('Let\'s run another 100,000 simulations.')
# simMatch = 0 # How many simulations had matching birthdays in them.
# for i in range(100_000):
#     # Report on the progress every 10,000 simulations:
#     if i % 10_000 == 0:
#         print(i, 'simulations run...')
#     birthdays = getBirthdays(numBDays)
#     if getMatch(birthdays) != None:
#         simMatch = simMatch + 1
# print('100,000 simulations run.')

# # Display simulation results:
# probability = round(simMatch / 100_000 * 100, 2)
# print('Out of 100,000 simulations of', numBDays, 'people, there was a')
# print('matching birthday in that group', simMatch, 'times. This means')
# print('that', numBDays, 'people have a', probability, '% chance of')
# print('having a matching birthday in their group.')
# print('That\'s probably more than you would think!')


# """
# ██████╗ ██╗████████╗███╗   ███╗ █████╗ ██████╗              
# ██╔══██╗██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗             
# ██████╔╝██║   ██║   ██╔████╔██║███████║██████╔╝             
# ██╔══██╗██║   ██║   ██║╚██╔╝██║██╔══██║██╔═══╝              
# ██████╔╝██║   ██║   ██║ ╚═╝ ██║██║  ██║██║                  
# ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝                  
                                                            
# ███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗
# ████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝
# ██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  
# ██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  
# ██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗
# ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
# """
# """Bitmap Message, by Al Sweigart al@inventwithpython.com
# Displays a text message according to the provided bitmap image.
# View this code at https://nostarch.com/big-book-small-python-projects
# Tags: tiny, beginner, artistic"""
# import sys

# # (!) Try changing this multiline string to any image you like:

# # There are 68 periods along the top and bottom of this string:
# # (You can also copy and paste this string from
# # https://inventwithpython.com/bitmapworld.txt)
# bitmap = """......................................................................
# ......................................................................
# ..........................................XXXXXXXX....................
# ......................................XXXXXXXXXX......................
# ....................................XXXXXXXXXXXX......................
# ...................................XXXXXXXXXXXXX......................
# ..................................XXXXXXXXXXXXXX......................
# .................................XXXXXXXXXXXXXXXX.....................
# .................................XXXXXXXXXXXXXXXX.....................
# .................................XXXXXXXXXXXXXXXXX....................
# .................................XXXXXXXXXXXXXXXXX....................
# .................................XXXXXXXXXXXXXXXXXX...................
# .................................XXXXXXXXXXXXXXXXXX...................
# .................................XXXXXXXXXXXXXXXXXXX..................
# .................................XXXXXXXXXXXXXXXXXXX..................
# .................................XXXXXXXXXXXXXXXXXXXX.................
# .................................XXXXXXXXXXXXXXXXXXXX.................
# .................................XXXXXXXXXXXXXXXXXXXXX................
# .................................XXXXXXXXXXXXXXXXXXXXX................
# .................................XXXXXXXXXXXXXXXXXXXXXX...............
# .................................XXXXXXXXXXXXXXXXXXXXXX...............
# .................................XXXXXXXXXXXXXXXXXXXXXXX..............
# .................................XXXXXXXXXXXXXXXXXXXXXXX..............
# .................................XXXXXXXXXXXXXXXXXXXXXXXX.............

# ...XXXXXXXXX....................XXXXXXXXXXXXXXXXXXXXXXXX.............
# ...XXXXXXXXXX...................XXXXXXXXXXXXXXXXXXXXXXXX.............
# ...XXXXXXXXXXX..................XXXXXXXXXXXXXXXXXXXXXXXX.............
# ...XXXXXXXXXXXX.................XXXXXXXXXXXXXXXXXXXXXXXX.............
# ...XXXXXXXXXXXX.................XXXXXXXXXXXXXXXXXXXXXXXX.............
# ...XXXXXXXXXXXXX................XXXXXXXXXXXXXXXXXXXXXXXX.............

# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................
# ......................................................................"""

# print('''Bitmap Message, by Al Sweigart
# Enter the message to display with the bitmap.
# You\'ll have to stick to capital letters and the space character.''')
# message = input('> ')

# if message == '':
#     sys.exit()

# # Loop over each line in the bitmap:
# for line in bitmap.splitlines():
#     # Loop over each character in the line:
#     for i, bit in enumerate(line):
#         if bit == 'X':
#             # Print an X for each bit that is set:
#             print(message[i % len(message)], end='')
#         else:
#             print(' ', end='') # Print a space otherwise.
#     print() # Print a newline.

# #write into a @hops component
# @hops.component(
#     "/bitmap",
#     name="Bitmap",
#     description="Display a text message according to the provided bitmap image.",
#     inputs=[
#         hs.HopsBoolean("Run", True),
#         ],
#     outputs=[
#         hs.HopsString("Message", "Hello World!"),
#         ],
#     )
# def bitmap(message):
#     import sys

#     # (!) Try changing this multiline string to any image you like:

#     # There are 68 periods along the top and bottom of this string:
#     # (You can also copy and paste this string from
#     # https://inventwithpython.com/bitmapworld.txt)
#     bitmap = """......................................................................
#     ......................................................................
#     ..........................................XXXXXXXX....................
#     ......................................XXXXXXXXXX......................
#     ....................................XXXXXXXXXXXX......................
#     ...................................XXXXXXXXXXXXX......................
#     ..................................XXXXXXXXXXXXXX......................
#     .................................XXXXXXXXXXXXXXXX.....................
#     .................................XXXXXXXXXXXXXXXX.....................
#     .................................XXXXXXXXXXXXXXXXX....................
#     .................................XXXXXXXXXXXXXXXXX....................
#     .................................XXXXXXXXXXXXXXXXXX...................
#     .................................XXXXXXXXXXXXXXXXXX...................
#     .................................XXXXXXXXXXXXXXXXXXX..................
#     .................................XXXXXXXXXXXXXXXXXXX..................
#     .................................XXXXXXXXXXXXXXXXXXXX.................
#     .................................XXXXXXXXXXXXXXXXXXXX.................
#     .................................XXXXXXXXXXXXXXXXXXXXX................
#     .................................XXXXXXXXXXXXXXXXXXXXX................
#     .................................XXXXXXXXXXXXXXXXXXXXXX...............
#     .................................XXXXXXXXXXXXXXXXXXXXXX...............
#     .................................XXXXXXXXXXXXXXXXXXXXXXX..............
#     .................................XXXXXXXXXXXXXXXXXXXXXXX..............
#     .................................XXXXXXXXXXXXXXXXXXXXXXXX.............

#     ...XXXXXXXXX....................XXXXXXXXXXXXXXXXXXXXXXXX.............
#     ...XXXXXXXXXX...................XXXXXXXXXXXXXXXXXXXXXXXX.............
#     ...XXXXXXXXXXX..................XXXXXXXXXXXXXXXXXXXXXXXX.............
#     ...XXXXXXXXXXXX.................XXXXXXXXXXXXXXXXXXXXXXXX.............
#     ...XXXXXXXXXXXX.................XXXXXXXXXXXXXXXXXXXXXXXX.............
#     ...XXXXXXXXXXXXX................XXXXXXXXXXXXXXXXXXXXXXXX.............

#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     .XXXXXXXXXXXX
#     ........................XXXXXXXXXXXXXXXXXX............................
#     ............................XXXXXXXXXXXXXX............................
#     ................................XXXXXXXXXX............................
#     ......................................................................
#     ......................................................................
#     ......................................................................
#     ......................................................................"""

#     print('''Bitmap Message, by Al Sweigart
#     Enter the message to display with the bitmap.
#     You\'ll have to stick to capital letters and the space character.''')
#     message = input('> ')

#     if message == '':
#         sys.exit()

#     # Loop over each line in the bitmap:
#     for line in bitmap.splitlines():
#         # Loop over each character in the line:
#         for i, bit in enumerate(line):
#             if bit == 'X':
#                 # Print an X for each bit that is set:
#                 print(message[i % len(message)], end='')
#             else:
#                 print(' ', end='')
#         print() # Print a newline.

"""
██╗      █████╗ ████████╗████████╗██╗ ██████╗███████╗
██║     ██╔══██╗╚══██╔══╝╚══██╔══╝██║██╔════╝██╔════╝
██║     ███████║   ██║      ██║   ██║██║     █████╗  
██║     ██╔══██║   ██║      ██║   ██║██║     ██╔══╝  
███████╗██║  ██║   ██║      ██║   ██║╚██████╗███████╗
╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝ ╚═════╝╚══════╝
"""            
#write a @hops component for a simple lattice structure
@hops.component(
    "/lattice_06",
    name="Lattice",
    description="Create a simple lattice structure.",
    inputs=[
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10)
        ],
    outputs=[
        hs.HopsPoint("Points", "Points")
        ],
    )
def lattice_06(size, spacing):
    #import rhino3dm
    import math
    
    #create a list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, 0))

    return points

#write a @hops component for a simple lattice structure
@hops.component(
    "/lattice_lines_01",
    name="Lattice Lines",
    description="Create a simple lattice structure.",
    inputs=[
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10)
        ],
    outputs=[
        hs.HopsMesh("Lines", "Lines")
        ],
    )
def lattice_lines_01(size, spacing):
    #import rhino3dm
    import math
    
    #create a list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, 0))

    #create a list of lines
    lines = []
    for i in range(size - 1):
        for j in range(size - 1):
            index = i * size + j
            lines.append(rhino3dm.LineCurve(points[index], points[index + 1]))
            lines.append(rhino3dm.LineCurve(points[index], points[index + size]))

    return lines

#write a @hops component for a simple lattice structure
@hops.component(
    "/lattice_mesh_06",
    name="Lattice Mesh",
    description="Create a simple lattice structure.",
    inputs=[
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10),
        hs.HopsInteger("Thickness", 1)
        ],
    outputs=[
        hs.HopsCurve("Mesh", "Mesh")
        ],
    )
def lattice_mesh_06(size, spacing, thickness):
    #import rhino3dm
    import math
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, thickness))

    #create a list of lines
    lines = []
    for i in range(size - 1):
        for j in range(size - 1):
            index = i * size + j
            lines.append(rhino3dm.LineCurve(points[index], points[index + 1]))
            lines.append(rhino3dm.LineCurve(points[index], points[index + size]))

    return lines
    
#write a @hops component for a simple lattice structure
@hops.component(
    "/lattice_trig_04",
    name="Lattice Trig",
    description="Create a simple lattice structure.",
    inputs=[
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10),
        hs.HopsNumber("Thickness", 1)
        ],
    outputs=[
        hs.HopsCurve("TrigCurves", "TrigCurves")
        ],
    )
def lattice_trig_04(size, spacing, thickness):
    #import rhino3dm
    import math
    #create trigonometric points with math.sin and math.cos functions
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, math.sin * 10 * thickness))
    #amplify and move the points with trigonometric functions
    for i in range(len(points)):
        points[i].X += math.sin(points[i].X) * 10
        points[i].Y += math.cos(points[i].Y) * 10
        points[i].Z += math.sin(points[i].Z) * 10

    #create a list of lines
    lines = []
    for i in range(size - 1):
        for j in range(size - 1):
            index = i * size + j
            lines.append(rhino3dm.LineCurve(points[index], points[index + 1]))
            lines.append(rhino3dm.LineCurve(points[index], points[index + size]))

    return lines


    















if __name__ == "__main__":
    app.run(debug=True)