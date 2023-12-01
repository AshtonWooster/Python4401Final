# Ashton Wooster
# Main

from Noise import Noise

# Main Function
def main():
    noise_grid = Noise()
    noise_grid.set_grid(noise_grid.noise())
    print(noise_grid)

main()
