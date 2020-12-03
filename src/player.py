import pygame
from ship import Ship
import sprite_handler as sprite
from main import HEIGHT, WIDTH

PLAYER_VELOCITY = 5
PLAYER_LASER_VEL = 6


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
        if keyDictionary[pygame.K_s] and self.y + self.velocity + super().getHeight() + 15 < HEIGHT:  # Down
            self.y += self.velocity
        if keyDictionary[pygame.K_SPACE]:
            self.shoot()

    def moveLasers(self, vel, objs):
        enemiesShot = 0
        self.updateCooldown()
        for laser in self.lasers:
            laser.moveLaser(vel)
            if laser.isOffScreen():
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        enemiesShot += 1
                        objs.remove(obj)
                        self.lasers.remove(laser)
        return enemiesShot

    def drawHealth(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.shipImg.get_height() + 10,
                                               self.shipImg.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.shipImg.get_height() + 10,
                                               (self.health / 100) * self.shipImg.get_width(), 10))