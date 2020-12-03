import pygame
from ship import Ship
import sprite_handler as sprite
from main import HEIGHT, WIDTH

ENEMY_VELOCITY = 7


class Enemy(Ship):
    COLOR_MAP = {
        "red": (sprite.RED_SHIP, sprite.RED_LASER),
        "blue": (sprite.GREEN_SHIP, sprite.GREEN_LASER),
        "green": (sprite.BLUE_SHIP, sprite.BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100, ):
        super().__init__(x, y, health, ENEMY_VELOCITY)
        self.shipImg, self.laserImg = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.shipImg)
        self.maxHealth = health

    def moveShip(self):
        self.y += ENEMY_VELOCITY
