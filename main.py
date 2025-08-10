# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():

    pygame.init()

    clock = pygame.time.Clock()         # Create a clock instance

    screen = pygame.display.set_mode((600, 400))  # Creates a 600x400 window

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # Create the player object

    pygame.display.set_caption("Test Pygame")

    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fills the screen black

        player.draw(screen)     # re-render player object on screen
        
        pygame.display.flip()   # Update the display

        # Get the time passed since the last frame
        # clock.tick() returns the milliseconds since the last call
        # Divide by 1000 to convert to seconds for physics calculations
        dt = clock.tick(60) / 1000      # Limits FPS to 60 and gets delta time

    pygame.quit()

    
if __name__ == "__main__":
     main()
