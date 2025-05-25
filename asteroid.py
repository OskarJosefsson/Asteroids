from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        angle = random.uniform(20,50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        aster_1 = Asteroid(self.position[0], self.position[1], radius)
        aster_2 = Asteroid(self.position[0], self.position[1], radius)
        aster_1.velocity = pygame.Vector2(self.velocity[0], self.velocity[1]).rotate(angle) * 1.2
        aster_2.velocity = pygame.Vector2(self.velocity[0], self.velocity[1]).rotate(-angle) * 1.2













