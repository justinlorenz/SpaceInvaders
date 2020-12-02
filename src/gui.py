import pygame
import sprite_handler
from progress import GameProgress

pygame.font.init()

LIVES_COLOR = (199, 0, 57)
LEVEL_COLOR = (219, 255, 51)


class MainUi:
    def __init__(self, game, width, height, fps):
        self.game = game
        self.width = width
        self.height = height
        self.fps = fps
        self.window = pygame.display.set_mode((self.width, self.height))
        self.mainFont = pygame.font.SysFont("comicsans", 50)
        self.progress = GameProgress()
        pygame.display.set_caption(self.game)

    def runGame(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.fps)
            self.updateWindow()
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False

    def updateWindow(self):
        self.window.blit(sprite_handler.BACKGROUND, (0, 0))
        livesLabel = self.mainFont.render(f"Lives: {self.progress.getLives()}", 1, LIVES_COLOR)
        levelLabel = self.mainFont.render(f"Level: {self.progress.getLevel()}", 1, LEVEL_COLOR)
        self.window.blit(livesLabel, (10, 10))
        self.window.blit(levelLabel, (self.width - levelLabel.get_width() - 10, 10))
        pygame.display.update()
