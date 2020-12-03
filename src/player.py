import pygame
from ship import Ship
import sprite_handler as sprite
from main import HEIGHT, WIDTH

PLAYER_VELOCITY = 5


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, PLAYER_VELOCITY, health)
        self.shipImg = sprite.YELLOW_SHIP
        self.laserImg = sprite.YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.shipImg)
        self.maxHealth = health

    def moveShip(self, keyDictionary):
        if keyDictionary[pygame.K_a] and self.x - self.velocity > 0:  # Left
            self.x -= self.velocity
        if keyDictionary[pygame.K_d] and self.x + self.velocity + super().getWidth() < WIDTH:  # Right
            self.x += self.velocity
        if keyDictionary[pygame.K_w] and self.y - self.velocity > 0:  # Up
            self.y -= self.velocity
        if keyDictionary[pygame.K_s] and self.y + self.velocity + super().getHeight() < HEIGHT:  # Down
            self.y += self.velocity
        if keyDictionary[pygame.K_SPACE]:
            self.shoot()
