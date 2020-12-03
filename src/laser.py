import pygame
import sprite_handler as sprite
from main import HEIGHT, WIDTH
from collide import Collide


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def drawLaser(self, window):
        window.blit(self.img, (self.x, self.y))

    def moveLaser(self, laserVel):
        self.y += laserVel

    def isOffScreen(self):
        return self.y > HEIGHT or self.y < 0 or self.x < 0 or self.y > WIDTH

    def collision(self, obj):
        return Collide(obj, self)
