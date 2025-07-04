import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize all imported pygame modules
    pygame.init()
    
    # initialize screen (GUI window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # init game "clock" for fps
    game_clock = pygame.time.Clock()
    dt = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # asteroids group, this is where the asteroids will be
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    # asteroid container
    Asteroid.containers = (asteroids, updatable, drawable)
    # asteroidfield container, only updatable
    AsteroidField.containers = (updatable)
    # init player to the middle of the screen
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y) 

    # init asteroidfield
    asteroi_dfield = AsteroidField()

    while True:
        # quit method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # filling the screen with black background color
        pygame.Surface.fill(screen, color="black")
        
        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        # check for asteroid player collision
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                sys.exit()

        # updates the screen
        pygame.display.flip()
        # 60 FPS
        dt = game_clock.tick(60) / 1000




if __name__ == "__main__":
    main()
