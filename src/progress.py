import pygame

WAVE_LENGTH_ADDITION = 5


class GameProgress:

    def __init__(self):
        self.lives = 3
        self.level = 0
        self.waveLength = 5
        self.enemyVel = 1

    def updateProgress(self, numEnemies):
        if numEnemies is 0:
            self.level += 1
            self.waveLength += WAVE_LENGTH_ADDITION
            return self.waveLength

    def getLives(self):
        return self.lives

    def getLevel(self):
        return self.level

    def getWaveLength(self):
        return self.waveLength

    def getEnemyVel(self):
        return self.enemyVel

    def updateWaveLength(self, count):
        self.waveLength += count

    def updateEnemyVel(self, increment):
        self.enemyVel += increment
