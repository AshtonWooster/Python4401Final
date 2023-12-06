# Ashton Wooster
# Main

from Noise import Noise
from Screen import Screen
import time

# TODO: The negative values arent working. I dont know why.

screen = Screen()

# Main Function
def main():
    noise_grid = Noise()
    noise_grid.set_grid(noise_grid.noise())
    screen.render_grid(noise_grid)
    screen.update_screen()
    time.sleep(10)

main()
