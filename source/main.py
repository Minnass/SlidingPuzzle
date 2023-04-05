import pygame
import random
import time
from  .GameSettings.Tile import Tile
from .GameSettings.settings import *
from .GameSettings.util import *
from .GameSettings.Board import Board
from enum import Enum


class Mode(Enum):
    HUMAN_MODE = 1
    SOLVER_MODE = 2


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.all_sprites = pygame.sprite.Group()
        self.board = Board(self, GAME_SIZE)
        self.border = Border(GAME_SIZE, self.screen)
        self.isPlaying = False

    def createGame(self):
        self.isPlaying = False
        self.Mode = Mode.HUMAN_MODEF

    # Tao tile
    def update(self):
        pass

    def draw(self):
        self.board.drawBoard()
        self.border.drawBorder()
        pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()


game = Game()

while True:
    game.draw()
