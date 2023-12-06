# Ashton Wooster
# Screen Class

from turtle import Turtle
import math

# Draw rectangle
def draw_rectangle(drawer, color, length, width):
    drawer.fillcolor(color)
    drawer.begin_fill()
    for i in range(4):
        # Draw box
        drawer.forward(i % 2 == 0 and width or length)
        drawer.right(90)
    drawer.end_fill()

# Screen Class
class Screen:
    # Constructor
    def __init__(self):
        turtle = Turtle()
        turtle.screen.tracer(0)
        # turtle.hideturtle()

        self.__turtle = turtle
    
    # Update screen
    def update_screen(self):
        self.__turtle.screen.update()
    
    # Render Grid
    def render_grid(self, noise):
        # Calcuate pixel size for the noise grid
        MARGINS = 10
        MENU_HEIGHT = 0

        noise_grid = noise.get_grid()
        length = len(noise_grid)
        width = len(noise_grid[0])
        w_height = self.__turtle.screen.window_height()
        w_width = self.__turtle.screen.window_width()
        l_pixel = (w_height - MARGINS * 3 - MENU_HEIGHT) / length
        w_pixel = (w_width - MARGINS * 2) / width 

        # Move turtle to top left
        self.__turtle.penup()
        self.__turtle.setpos(MARGINS - w_width/2, w_height/2 - MARGINS)

        for x in range(length):
            for y in range(width):
                # Draw each pixel
                value = (noise_grid[x][y]+1)/2
                draw_rectangle(self.__turtle, (value, value, value), l_pixel, w_pixel)
                self.__turtle.forward(w_pixel)
            # Move to next row
            self.__turtle.right(90)
            self.__turtle.forward(l_pixel)
            self.__turtle.left(90)
            self.__turtle.backward(w_pixel * width)

            