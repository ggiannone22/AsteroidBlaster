from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: object) -> None:                         # Draws the bullet
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:                            # Updates the position relative to its velocity also using delta time
        self.position += (self.velocity * dt)
