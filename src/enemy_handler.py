import random
from main import HEIGHT, WIDTH
from enemy import Enemy
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

    def moveEnemies(self):
        livesLost = 0
        for enemy in self.enemies:
            enemy.moveShip()
            if enemy.y + enemy.getHeight() > HEIGHT:
                livesLost += 1
                self.enemies.remove(enemy)

        return livesLost


        print(f"Enemy 1 y value {self.enemies[0].y}")

    def getNumOfEnemies(self):
        return len(self.enemies)

    def getEnemies(self):
        return self.enemies
