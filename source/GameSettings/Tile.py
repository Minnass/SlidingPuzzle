import pygame
from pygame.sprite import Sprite
from settings import *

class Tile(Sprite):
    def __init__(self, row, col, image_path, sprite_groups,TileSize):
        Sprite.__init__(self, sprite_groups)
        self.TileSize=TileSize
        self.row, self.col, self.image_path = row, col, image_path
        if (image_path != 'empty'):
            bitmaps = pygame.image.load(self.image_path).convert()
            self.image = pygame.transform.smoothscale(
                bitmaps, (self.Tile, self.Tile))
        else:
            self.image = pygame.Surface((self.Tile, self.Tile))
            self.image.fill(BACKGROUND_COLOR)
        self.rect = self.image.get_rect()

    def getPosition(self):
        return (self.row, self.col)

    def setPosition(self, newPosition:tuple):
        self.row = newPosition[0]
        self.col = newPosition[1]
    
    def update(self):
        self.rect.x=self.Tile*self.row
        self.rect.y=self.Tile*self.col
    
    def getCoordinates(self):
        return (self.Tile*self.row,self.Tile*self.col)

            
        