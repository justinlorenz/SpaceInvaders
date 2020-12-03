import pygame


class Ship:
    def __init__(self, x, y, health, velocity):
        self.x = x
        self.y = y
        self.health = health
        self.velocity = velocity
        self.shipImg = None
        self.laserImg = None
        self.lasers = []
        self.cooldown = 0

    def getWidth(self):
        return self.shipImg.get_width()

    def getHeight(self):
        return self.shipImg.get_height()

    def drawShip(self, window):
        window.blit(self.shipImg, (self.x, self.y))

