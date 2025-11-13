import pygame
import constants
import random
from logger import log_event
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(angle)
        direction2 = self.velocity.rotate(-angle)
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = direction1 * 1.2
        child2.velocity = direction2 * 1.2

