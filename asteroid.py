from circleshape import CircleShape
from constants import *
import pygame 
from logger import *
import random

class Asteroid(CircleShape):                                                # Class for the Asteroids

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: object) -> None:                                 # Draws the Asteroids
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:                                    # Updates the position relative to its velocity also using delta time
        self.position += (self.velocity * dt)

    def split(self) -> None:                                                # Splits Asteroids into 2 if shot;
        self.kill()                                                         # Kills original asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:                              # If asteroid is smallest asteorid, do nothing 
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)                                      # Create a random angle between 20-50 degrees
        new_velocity_1 = self.velocity.rotate(angle)                        # Create the new velocity vector using the random angle
        new_velocity_2 = self.velocity.rotate(-angle)                       # Same idea but with a negative angle on the opposite side
        new_radius = self.radius - ASTEROID_MIN_RADIUS                      # Create the new asteroid radius by the next smallest asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)  # Creating Astroid instances using current position of original asteroid and new radius
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1 * 1.2                           # Upscale velocity to make new asteroid faster
        asteroid2.velocity = new_velocity_2 * 1.2 
