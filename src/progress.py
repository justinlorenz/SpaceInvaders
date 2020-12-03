import pygame

WAVE_LENGTH_ADDITION = 5


class GameProgress:

    def __init__(self):
        self.lives = 3
        self.level = 0
        self.waveLength = 0
        self.enemyVel = 1

    def isLevelBeaten(self, numEnemies):
        if numEnemies is 0:
            self.level += 1
            self.waveLength += WAVE_LENGTH_ADDITION
            self.enemyVel += 1
            return True
        return False

    def isGameLost(self):
        return self.lives <= 0

    def loseLives(self, livesLost):
        self.lives -= livesLost

    def getLives(self):
        return self.lives

    def getLevel(self):
        return self.level

    def getWaveLength(self):
        return self.waveLength

    def getEnemyVel(self):
        return self.enemyVel


