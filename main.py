import pygame
import sys
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from circleshape import * 
from logger import log_state, log_event

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 40)
running = True
black = (0, 0, 0)
clock = pygame.time.Clock()
#main menu
def main_menu(last_score=None):
    global running
    while running:
        screen.fill((0, 0, 0))

        title_text = font.render("ASTEROIDS", True, (255, 255, 255))
        start_text = small_font.render("Press ENTER to Play", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3)))
        screen.blit(start_text, start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))
        screen.blit(quit_text, quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60)))
        
        if last_score is not None:
            score_text = small_font.render(f"Last Score: {last_score}", True, (255, 255, 0))
            screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 120)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        clock.tick(60)

#main game loop        
def main():
    global running
    dt = 0
    score = 0
    score_font = pygame.font.Font(None, 36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    AsteroidField()



    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                main_menu(last_score=score)
        for a in asteroids:
            for shot in shots:
                if a.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    a.split()
                    score += int(100 / a.radius)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        pygame.display.flip()


        dt = clock.tick(60) / 1000.0
        


                             
            
        
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main_menu()
