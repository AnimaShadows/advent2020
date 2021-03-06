#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")
   x = 0
   for line in f:
      puzzle_input.append([])
      for char in range (0, len(line)):
         puzzle_input[x].append(line[char])
      x += 1

   f.close()

   #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
   #   for row in puzzle_input]))

   return puzzle_input


def countTrees(puzzle_input):
   i = 0
   j = 0
   numTrees = 0

   #for x in range(0,len(puzzle_input),1):
   #   for j in range (0,len(puzzle_input[i]),3):
   #      if (puzzle_input[i][j] == "#"):
   #         numTrees += 1
   while i < len(puzzle_input) - 1:
      i += 1
      j = (j + 3) % 31
      if (puzzle_input[i][j] == "#"):
         numTrees += 1


   return numTrees


def main():
   puzzle_input = populate()

   numTrees = countTrees(puzzle_input)

   print("Number of Trees: " + str(numTrees))

if __name__ == "__main__":
   main()
