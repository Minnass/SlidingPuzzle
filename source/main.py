import pygame
import random
import time
from Tile import *
from settings import *
from util import *
from Board import *
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.all_sprites=pygame.sprite.Group()
        self.board=Board(self)
        self.border=Border(GAME_SIZE ,self.screen)
        # self.tiles=[]
        # self.tile_grids=[]
        # self.imageDivider=ImageDivider(,3)
    def createGame(self):
        for row in range(1,GAME_SIZE+1):
            self.tile_grids.append([])
            for col in range(1,1+GAME_SIZE):
                self.tile_grids[row-1].append((row-1)*GAME_SIZE+col)
        self.tile_grids[-1][-1]=0
              
        #Tao tile

    def draw(self):
        self.all_sprites.draw()
        self.border.drawBorder()
        pygame.display.flip()
    