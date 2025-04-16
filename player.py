from circleshape import CircleShape
from constants import *
import pygame
class Player(CircleShape):
    rotation = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return super().draw(screen)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    '''
    If we press the move-left key, the ship should rotate to the left.
    If we press the move-right key, the ship should rotate to the right.
    If we press the move-forward key, the ship should move forward.
    If we press the move-backward key, the ship should move backward.
    '''
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # move left
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        # move right
        if keys[pygame.K_d]:
            self.rotate(dt)
        # move up
        if keys[pygame.K_w]:
            self.move(dt * -1)
        # move down
        if keys[pygame.K_s]:
            self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt