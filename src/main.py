import pygame
import os
import time
import random
from gui import *

GAME_NAME = "Space Invaders"
WIDTH, HEIGHT = 800, 800
FPS = 60


def main():
    gui = MainUi(GAME_NAME, WIDTH, HEIGHT, FPS)
    gui.runGame()


if __name__ == "__main__":
    main()
