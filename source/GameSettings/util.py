import pygame
import cv2
import os


class Border():
    def __init__(self, game_size, sceen_surface, tileSIze, color):
        self.game_size = game_size
        self.screen_surface = sceen_surface
        self.tileSize = tileSIze
        self.color = color

    def drawBorder(self):
        for row in range(-1, self.tileSize*self.game_size, self.tileSize):
            pygame.draw.line(self.screen_surface, self.color,
                             (0, row), (self.game_size*self.tileSize, row))
        for col in range(-1, self.game_size*self.tileSize, self.tileSize):
            pygame.draw.line(self.screen_surface, self.color,
                             (col, 0), (col, self.game_size*self.tileSize))


class Image():
    def __init__(self, path) -> None:
        self.path = path
        print(path)
        if (self.isExist()):
            self.bitmaps=cv2.imread(self.path)
            self.h,self.w,self.channels=self.bitmaps.shape
        else:
            self.bitmaps = None

    def isExist(self):
        if (not os.path.isfile(self.path)):
            return False
        return True
    def getHeight(self):
        return self.h
    def getWidth(self):
        return self.w
    def getChannels(self):
        return self.channels
    def getBitMap(self):
        return self.bitmaps


class ImageDivider():
    def __init__(self, img: Image, gameSize,dst_folder) -> None:
        self.img = img
        self.gameSize = gameSize
        self.divided_img_path = []
        self.dst_folder=dst_folder

    def divideImage(self):
        divivedSize = self.img.getHeight()//self.gameSize
        for row in range(1, self.gameSize+1):
            for col in range(1, self.gameSize+1):
                if (((row-1)*self.gameSize+col) != self.gameSize*self.gameSize):
                    fileName = f'{(row-1)*self.gameSize+col}.png'
                    self.divided_img_path.append(self.dst_folder+fileName)
                    self.exportToFile(self.dst_folder+fileName, self.img.getBitMap()[(row-1)*divivedSize:row*divivedSize,
                                                    (col-1)*divivedSize:divivedSize*(col)])

    def exportToFile(self,fileName,bitmap):
     
        cv2.imwrite(fileName,bitmap)

    def getAllPath(self):
        return self.divided_img_path

