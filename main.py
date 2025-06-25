import pygame
from constants import *
from player import *

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

    # init player to the middle of the screen
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    while True:
        # quit method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # filling the screen with black background color
        pygame.Surface.fill(screen, color="black")
        
        # drawing player
        player.draw(screen)
        
        # update the player
        player.update(dt)


        # updates the screen
        pygame.display.flip()
        # 60 FPS
        dt = game_clock.tick(60) / 1000




if __name__ == "__main__":
    main()
