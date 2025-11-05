import pygame
from constants import *
from player import Player
from circleshape import * 

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
black = (0, 0, 0)
clock = pygame.time.Clock()
dt = 0 

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
         
def main():
    global running
    while running:
        fps = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        


                             
            
        
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
