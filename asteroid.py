import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = None  # This will be set in the main file
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt  # Example movement
    
    def split(self):
        self.kill()

        if(self.radius <= ASTEROID_MIN_RADIUS):
            #this is the smallest asteroid so we don't split it
            return
        
        random_angle = random.uniform(20, 50)
        asteroid_split1 = self.velocity.rotate(random_angle)
        asteroid_split2 = self.velocity.rotate(-random_angle)
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid1_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid2_radius)
        asteroid1.velocity = asteroid_split1 * 1.2
        asteroid2.velocity = asteroid_split2 * 1.2