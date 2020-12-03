import pygame
from main import FPS
from laser import Laser


class Ship:
    COOLDOWN = FPS / 2

    def __init__(self, x, y, velocity, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.velocity = velocity
        self.shipImg = None
        self.laserImg = None
        self.lasers = []
        self.cooldown = 0

    def shoot(self):
        if self.cooldown == 0:
            self.lasers.append(Laser(self.x, self.y, self.laserImg))
            self.cooldown = 1

    def updateCooldown(self):
        if self.cooldown >= self.COOLDOWN:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def getWidth(self):
        return self.shipImg.get_width()

    def getHeight(self):
        return self.shipImg.get_height()

    def moveLasers(self, vel, obj):
        self.updateCooldown()
        for laser in self.lasers[:]:
            laser.moveLaser(vel)
            if laser.isOffScreen():
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def drawShip(self, window):
        window.blit(self.shipImg, (self.x, self.y))
        for laser in self.lasers:
            laser.drawLaser(window)

