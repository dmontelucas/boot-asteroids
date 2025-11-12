import pygame
import constants
from shot import *
from circleshape import *



class Player(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position
        self.radius = constants.PLAYER_RADIUS
        self.rotation = 0
        self.shoot_cooldown_timer = 0

    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.polygon(screen, color, self.triangle(),constants.LINE_WIDTH)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        vel = direction * constants.PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot.velocity = vel
        self. shoot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS



    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt
