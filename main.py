import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creates a 600x400 window

    pygame.display.set_caption("Test Pygame")
    
    clock = pygame.time.Clock()         # Create a clock instance

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Create asteroid container membership
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()                        # Create the asteroid field

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # Create the player object

    running = True
    dt = 0

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)        # update the updateable group to reflect movement

        for asteroid in asteroids:
            if asteroid.collision_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision_with(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")        # Fills the screen black
        
        for obj in drawable:
            obj.draw(screen)        # re-render all objects on screen

        pygame.display.flip()       # Update the display

        # Get the time passed since the last frame
        # clock.tick() returns the milliseconds since the last call
        # Divide by 1000 to convert to seconds for physics calculations
        dt = clock.tick(60) / 1000      # Limits FPS to 60 and gets delta 
        

    pygame.quit()

    
if __name__ == "__main__":
     main()
