from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape): # Player class

    def __init__(self, x: float, y: float) -> None:        # Position of player
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:        # Draws a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: object) -> None:             # Draws player (as a triangle)
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:                # updates rotation of character based on delta time
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt: float) -> None:                # Everytime a specific movement key is pressed, the corresponding movement happens
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate((-1 * dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((-1 * dt))
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt) -> None:                         #Added the physics to move up and down; created a vector, rotate vector using players rotation,
        unit_vector = pygame.Vector2(0,1)               #calc vector on how much player would move in the frame, update position with calculated vector
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:                            # Allows player to shoot; Creates a shot instance using the position of player, creates a unit vector,
        shot = Shot(self.position.x, self.position.y)   # Rotates the vector to face the player's direction, updates the velocity with PLAYER_SHOT_SPEED
        unit_vector = pygame.Vector2(0,1)
        rotate_with_player = unit_vector.rotate(self.rotation)
        shot.velocity = rotate_with_player * PLAYER_SHOOT_SPEED

