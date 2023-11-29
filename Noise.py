# Ashton Wooster
# 11.28.23
# Noise Class for generating a perlin noise grid

import random
import math

# Characters for printing ordered by brightness I got from Paul Bourke
#brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
brightness = " -.:=*+#%@"

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
    def fill_grid(self, frequency=4, amplitude=2):
        length = len(self.__grid)
        width = len(self.__grid[0])

        # Create permutation table
        max_length = length*width
        permutations = [i for i in range(max_length)]
        random.shuffle(permutations)
    
        # Create Influence Vectors
        influence_vectors = []
        i_length = math.ceil(length/frequency)
        i_width = math.ceil(width/frequency)
        for x in range(i_length):
            # Add a new row
            influence_vectors.append([])
            for y in range(i_width):
                # Assign x, y, and z to a random number between 0 and 1
                vector_x = permutations[x * i_length + y] / max_length
                vector_y = permutations[x * i_length + y + 1] / max_length
                vector_z = permutations[x * i_length + y + 2] / max_length
                influence_vectors[x].append((vector_x, vector_y, vector_z))

        for x in range(length):
            for y in range(width):
                self.__grid[x][y] = (x + y) / (length + width - 1)
