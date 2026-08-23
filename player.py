from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH
import pygame

class Player(CircleShape): # Player class

    def __init__(self, x: int, y: int) -> None:        # Position of player
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:        # Draws a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: object):                     # Draws player (as a triangle)
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
