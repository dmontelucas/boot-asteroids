import pygame
from constants import *
from player import Player
from circleshape import * 
import logger

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
black = (0, 0, 0)
clock = pygame.time.Clock()

         
def main():
    global running
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while running:
        logger.log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0
        


                             
            
        
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
