# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creates a 600x400 window

    clock = pygame.time.Clock()         # Create a clock instance

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create player group containers
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # Create the player object

    pygame.display.set_caption("Test Pygame")

    running = True
    dt = 0

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateable.update(dt)       # update the updateable group to reflect movement

        screen.fill("black")  # Fills the screen black

        for obj in drawable:
            obj.draw(screen)     # re-render all objects on screen

        pygame.display.flip()   # Update the display

        # Get the time passed since the last frame
        # clock.tick() returns the milliseconds since the last call
        # Divide by 1000 to convert to seconds for physics calculations
        dt = clock.tick(60) / 1000      # Limits FPS to 60 and gets delta 
        

    pygame.quit()

    
if __name__ == "__main__":
     main()
