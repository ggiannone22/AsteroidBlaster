from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame 

class Asteroid(CircleShape):                # Class for the Asteroids

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: object) -> None:             # Draws the Asteroids
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:                # Updates the position relative to its velocity also using delta time
        self.position += (self.velocity * dt)
