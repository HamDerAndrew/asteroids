from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SHOT_RADIUS
import pygame

class Shot(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or \
           self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()
        self.position += self.velocity * dt