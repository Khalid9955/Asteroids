import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius 
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        
        vectorClockwise = self.velocity.rotate(angle)
        vectorCounterClockwise = self.velocity.rotate(-angle)
        
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        
        newAsteroidClockwise = Asteroid(self.position.x, self.position.y, newRadius)
        newAsteroidCounterClockwise = Asteroid(self.position.x, self.position.y, newRadius)
        
        newAsteroidClockwise.velocity = vectorClockwise * 1.2
        newAsteroidCounterClockwise.velocity = vectorCounterClockwise * 1.2

