import pygame
from pygame.sprite import Sprite
from settings import *
import cv2
class Tile(Sprite):
    def __init__(self, row, col, image_path, sprite_groups):
        Sprite.__init__(self, sprite_groups)
        self.row, self.col, self.image_path = row, col, image_path
        if (image_path != 'empty'):
            bitmaps = pygame.image.load(self.image_path).convert()
            self.image = pygame.transform.smoothscale(
                bitmaps, (TILESIZE, TILESIZE))
        else:
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill(BACKGROUND_COLOR)
        self.rect = self.image.get_rect()

    def getPosition(self):
        return (self.row, self.col)

    def setPosition(self, newPosition:tuple):
        self.row = newPosition[0]
        self.col = newPosition[1]
    
    def update(self):
        self.rect.x=TILESIZE*self.col
        self.rect.y=TILESIZE*self.row

    def getCoordinates(self):
        return (TILESIZE*self.row,TILESIZE*self.col)

            
        