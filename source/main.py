import pygame
import random
import time
from Tile import *
from settings import *
from util import *
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.all_sprites=pygame.sprite.Group()
        self.border=Border(GAME_SIZE ,self.screen)
        self.tile=[]
    def createGame(self):
        #Tao tile
    
    def draw(self):
        #draw tiles
        #draw border
            
        pygame.display.flip()
    