from Tile import *
import pygame

class Board():
    def __init__(self, all_sprites:pygame.sprite.Group, gameSize) -> None:
        self.all_sprites = all_sprites
        self.gameSiZe = gameSize
        self.sourceGrids = []
        self.goalGrids = []
        self.Tiles = []
        self.emptyTilePosition = self.gameSiZe*self.gameSiZe-1

    def createBoard(self):

        for row in range(1, 1+self.gameSiZe):
            self.sourceGrids.append([])
            self.goalGrids.append([])
            for col in range(1, 1+self.gameSiZe):
                self.sourceGrids[row-1].append((row-1)*self.gameSiZe+col)
                self.goalGrids[row-1].append((row-1)*self.gameSiZe+col)
        self.sourceGrids[-1][-1] = 0
        self.goalGrids[-1][-1] = 0

        for row in range(self.gameSiZe):
            for col in range(self.gameSiZe):
                if (self.gameSiZe*row+col != self.gameSiZe*self.gameSiZe-1):
                    self.Tiles.append(
                        Tile(row, col, self.TileImages[row*self.gameSiZe+col], self.all_sprites))
                else:
                    self.Tiles.append(
                        Tile(row, col, 'empty', self.all_sprites))

    

    def getNeighboringTilles(self):
        row, col = self.Tiles[self.emptyTilePostion].getPosition()
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
        self.all_sprites.draw()

    def shuffle(self):
        pass

    def setTileImages(self, paths):
        self.TileImages = paths

    def isFinishGame(self):
        if (self.sourceGrids == self.goalGrids):
            return True
        else:
            return False
    def getEmptyTile(self):
        return self.Tiles[self.emptyTilePosition]
