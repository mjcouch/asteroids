# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((600, 400))  # Creates a 600x400 window
    pygame.display.set_caption("Test Pygame")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fills the screen white
        pygame.display.flip()

    pygame.quit()

    
    if __name__ == "__main__":
        main()
