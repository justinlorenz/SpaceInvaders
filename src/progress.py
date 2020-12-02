import pygame


class GameProgress:

    def __init__(self):
        self.lives = 3
        self.level = 1

    def getLives(self):
        return self.lives

    def getLevel(self):
        return self.level
