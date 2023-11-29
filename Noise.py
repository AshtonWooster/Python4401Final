# Ashton Wooster
# 11.28.23
# Noise Class for generating a perlin noise grid

import random
import math

# Characters for printing ordered by brightness I got from Paul Bourke
brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Noise Class
class Noise:
    # Constructor
    def __init__(self, length=50, width=50):
        self.__grid = [[0]*length for _ in range(width)]

    # To String
    def __str__(self):
        grid_display = ""

        # Format grid as string
        for x in range(len(self.__grid)):
            for y in range(len(self.__grid[0])):
                grid_display += (brightness[math.floor(self.__grid[x][y] * len(brightness))]) + " "
            grid_display += "\n"

        return grid_display

    # Populate grid
    def fill_grid(self, scale=4):
        length = len(self.__grid)
        width = len(self.__grid[0])

        # Create permutation table

        for x in range(length):
            for y in range(width):
                self.__grid[x][y] = (x + y) / (length + width - 1)
