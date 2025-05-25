from circleshape import CircleShape
import pygame
import constants
from shot import Shot

class Player (CircleShape):
    def __init__(self, x , y, shots):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.x = x
        self.y = y
        self.timer = 0



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2 )

    def rotate (self, dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer = self.timer - dt

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

        
    def move (self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot (self):

        if self.timer <= 0:
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position[0], self.position[1], constants.SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = shot.velocity * constants.PLAYER_SHOOT_SPEED
            self.shots.add(shot)


        



        

