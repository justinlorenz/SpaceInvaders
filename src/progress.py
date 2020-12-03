import pygame

WAVE_LENGTH_ADDITION = 3


class GameProgress:

    def __init__(self):
        self.lives = 5
        self.level = 0
        self.waveLength = 0
        self.enemyVel = 1
        self.enemyLaserVel = 2
        self.score = 0

    def isLevelBeaten(self, numEnemies):
        if numEnemies is 0:
            self.level += 1
            self.waveLength += WAVE_LENGTH_ADDITION
            if self.level % 3 == 0 and self.level != 0:
                self.enemyVel += 1
            self.enemyLaserVel += 1
            return True
        return False

    def addScore(self, scoreAmount):
        self.score += scoreAmount

    def getScore(self):
        return self.score

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

    def getEnemyLaserVel(self):
        return self.enemyLaserVel


