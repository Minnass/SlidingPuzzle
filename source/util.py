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


class ImageDivider():
    def __init__(self, imagePath, gameSize) -> None:
        self.imagePath = imagePath
        self.gameSize = gameSize
        self.divided_img_path = []

    def divideImage(self):
        img = cv2.imread(self.imagePath)
        h, w, channels = img.shape
        divivedSize = h//self.gameSize
        for row in range(1, self.gameSize+1):
            for col in range(1, self.gameSize+1):
                if (((row-1)*self.gameSize+col) != self.gameSize*self.gameSize):
                    fileName= f'{(row-1)*self.gameSize+col}.png'
                    self.divided_img_path.append(r'../image'+fileName)
                    self.exportToFile(fileName,img[(col-1)*divivedSize:col*divivedSize,
                                        (row-1)*divivedSize:divivedSize*(row)])

    def exportToFile(self, fileName, img):
        # dst_path = r'../source/'+fileName
        
        path = '../image'
        cv2.imwrite(os.path.join(path , fileName), img)
    def getAllPath(self):
        return self.divided_img_path


i = ImageDivider("../image/a.png", 2)

pygame.init()
screen = pygame.display.set_mode((500,800))
i.divideImage()
for a in i.getAllPath():
    print(a)
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

