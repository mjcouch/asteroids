# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    running = False

    while running == True:
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen black
        screen.fill((0, 0, 0))

        pygame.display.flip()
    
    

    if __name__ == "__main__":
        main()
