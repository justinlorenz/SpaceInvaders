import pygame
import sprite_handler
from progress import GameProgress
from player import Player
from enemy_handler import EnemyHandler
from ship import Ship

pygame.font.init()

LIVES_COLOR = (199, 0, 57)
LEVEL_COLOR = (219, 255, 51)
LOST_COLOR = (255, 255, 255)


class MainUi:

    def __init__(self, game, width, height, fps):
        self.game = game
        self.width = width
        self.height = height
        self.fps = fps
        self.window = pygame.display.set_mode((self.width, self.height))
        self.mainFont = pygame.font.SysFont("comicsans", 50)
        self.loseFont = pygame.font.SysFont("comicsans", 60)
        self.progress = GameProgress()
        self.player = Player(300, 650, 100)
        self.enemyHandler = EnemyHandler()
        self.lost = False
        self.lostCount = 0
        pygame.display.set_caption(self.game)

    def runGame(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.fps)

            # Check if game is lost
            if self.progress.isGameLost() or self.player.health <= 0:
                self.lost = True
                self.lostCount += 1

            # Exit the game if shown lost game screen for more than 3 seconds
            if self.lost and self.lostCount > self.fps * 3:
                run = False

            # Quit game if run is false
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False

            # Create new enemies if level beaten
            if self.progress.isLevelBeaten(self.enemyHandler.getNumOfEnemies()):
                self.enemyHandler.createNewEnemies(self.progress.getWaveLength(), self.progress.getEnemyVel())
            self.updateWindow()

    def updateWindow(self):
        self.window.blit(sprite_handler.BACKGROUND, (0, 0))
        self.drawText()
        if not self.lost:
            self.player.moveShip(pygame.key.get_pressed())
            self.progress.loseLives(self.enemyHandler.moveEnemies())
            self.player.drawShip(self.window)
            self.drawEnemies()
        pygame.display.update()

    def drawText(self):
        if self.lost:
            lostLabel = self.mainFont.render("You Lost!!", 1, LOST_COLOR)
            self.window.blit(lostLabel, (self.width / 2 - lostLabel.get_width() / 2, 350))
        livesLabel = self.mainFont.render(f"Lives: {self.progress.getLives()}", 1, LIVES_COLOR)
        levelLabel = self.mainFont.render(f"Level: {self.progress.getLevel()}", 1, LEVEL_COLOR)
        self.window.blit(livesLabel, (10, 10))
        self.window.blit(levelLabel, (self.width - levelLabel.get_width() - 10, 10))

    def drawEnemies(self):
        enemies = self.enemyHandler.getEnemies()
        for enemy in enemies:
            enemy.drawShip(self.window)
