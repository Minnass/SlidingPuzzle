from GameSettings.Tile import Tile
import pygame
from GameSettings.util import *

class Board():
    def __init__(self, all_sprites:pygame.sprite.Group, gameSize,screen) -> None:
        self.all_sprites = all_sprites
        self.gameSiZe = gameSize
        self.goalGrids = []
        self.currentGrids = []
        self.Tiles = []
        self.emptyTilePosition = self.gameSiZe*self.gameSiZe-1
        self.screen=screen

    def createBoard(self,dividedImagepaths):
        self.setTileImages(dividedImagepaths)
        for row in range(1, 1+self.gameSiZe):
            self.goalGrids.append([])
            self.currentGrids.append([])
            for col in range(1, 1+self.gameSiZe):
                self.goalGrids[row-1].append((row-1)*self.gameSiZe+col)
                self.currentGrids[row-1].append((row-1)*self.gameSiZe+col)
        self.goalGrids[-1][-1] = 0
        self.currentGrids[-1][-1] = 0

        for row in range(self.gameSiZe):
            for col in range(self.gameSiZe):
                if (self.gameSiZe*row+col != self.gameSiZe*self.gameSiZe-1):
                    self.Tiles.append(Tile(row, col, self.TileImages[row*self.gameSiZe+col], self.all_sprites))
                   
                else:
                    self.Tiles.append(
                        Tile(row, col, 'empty', self.all_sprites))

    def swap(self,value1:tuple,value2:tuple):
        _temp=self.currentGrids[value1[0]][value1[1]]
        self.currentGrids[value1[0]][value1[1]]=self.currentGrids[value2[0]][value2[1]]
        self.currentGrids[value2[0]][value2[1]]=_temp
    def getNeighboringTilles(self):
        row, col = self.Tiles[self.emptyTilePosition].getPosition()
        up = (row-1, col) if row-1 >= 0 else None
        down = (row+1, col) if row+1 < self.gameSiZe else None
        left = (row, col-1) if col - 1 >= 0 else None
        right = (row, col+1) if col + 1 < self.gameSiZe else None
        directions = [up, down, left, right]
        neighbors = []
        for dir in directions:
            if dir is not None:
                neighbors.append(dir)
        return neighbors

    def updateBoard(self):
        self.all_sprites.update()

    def drawBoard(self):
        self.all_sprites.draw(self.screen)

    def setTileImages(self, paths):
        self.TileImages = paths

    def isWin(self):
        if (self.goalGrids == self.currentGrids):
            return True
        else:
            return False
    def getEmptyTile(self):
        return self.Tiles[self.emptyTilePosition]
    def getAllTiles(self):
        return self.Tiles

