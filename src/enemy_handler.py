import random
from main import HEIGHT, WIDTH, FPS
from enemy import Enemy
from collide import Collide

import pygame
import sprite_handler
from progress import GameProgress


class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def createNewEnemies(self, waveLength, enemyVel):
        for i in range(waveLength):
            self.enemies.append(Enemy(random.randrange(50, WIDTH - 100), random.randrange(-HEIGHT * 2, -100),
                                      random.choice(["red", "blue", "green"]), enemyVel))

    def moveEnemies(self, player):
        livesLost = 0
        for enemy in self.enemies[:]:
            enemy.moveShip()
            if random.randrange(0, 4 * FPS) == 1:
                enemy.shoot()
            if Collide(enemy, player):
                player.health -= 10
                self.enemies.remove(enemy)
            elif enemy.y + enemy.getHeight() > HEIGHT:
                livesLost += 1
                self.enemies.remove(enemy)
        return livesLost

    def getNumOfEnemies(self):
        return len(self.enemies)

    def getEnemies(self):
        return self.enemies
