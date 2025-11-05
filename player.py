import pygame
import constants
from circleshape import *


class Player(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self_x = x
        self_y = y
        self.radius = constants.PLAYER_RADIUS
        self.rotation = 0

    def draw(self, screen):
        color = (255, 255, 255)
        line_width = 2
        pygame.draw.polygon(screen, color, self.triangle(),)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 