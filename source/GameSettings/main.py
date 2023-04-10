import pygame
import random
import time
from settings import *
from util import ImageDivider, Image
from Board import Board
from enum import Enum
from HummanResolver import *
from DFS import *
from BFS import *
from AStar import *
from UIElement import *


class Mode(Enum):
    HUMAN_MODE = 1
    SOLVER_MODE = 2


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.board = Board(pygame.sprite.Group(), GAME_SIZE, self.screen)
        self.border = Border(GAME_SIZE, self.screen, TILESIZE, LIGHTGREY)
        self.isPlaying = False
        self.isShuffle=False
        self.countShuffle=0
        self.buttons_list = []
        self.buttons_list.append(Button(TILESIZE*GAME_SIZE+TILESIZE,TILESIZE*3/2, 200, 50, "Shuffle", WHITE, BLACK))
        self.buttons_list.append(Button(TILESIZE*GAME_SIZE+TILESIZE,TILESIZE*2, 200, 50, "HUMAN-MODE", WHITE, BLACK))
        self.buttons_list.append(Button(TILESIZE*GAME_SIZE+TILESIZE,TILESIZE*5/2, 200, 50, "DFS", WHITE, BLACK))
        self.buttons_list.append(Button(TILESIZE*GAME_SIZE+TILESIZE,TILESIZE*3, 200, 50, "BFS", WHITE, BLACK))
        self.buttons_list.append(Button(TILESIZE*GAME_SIZE+TILESIZE,TILESIZE*7/2, 200, 50, "A*", WHITE, BLACK))
    def chooseImage(self):
        img = Image(IMAGES_FOLDER+'c.png')
        self.divider = ImageDivider(img, GAME_SIZE, IMAGES_FOLDER)
        self.divider.divideImage()
        return self.divider.getAllPath()

    def createGame(self):
        for btn in self.buttons_list:
            btn.draw(self.screen)
        self.elapsed_time=0
        
        self.isPlaying = False
        self.Mode = Mode.HUMAN_MODE
        self.board.createBoard(self.chooseImage())
        self.board.updateBoard()
        self.HumanResolver = HumanSolver(self.board)

    # Tao tile
    def shuffle(self):
        if(self.countShuffle==SHUFFLE):
            self.isShuffle=False
            self.countShuffle=0
            self.isPlaying=True
            self.startTime=time.time()
           
        else:
            neightbors=self.board.getNeighboringTilles()
            newEmptyPosition=random.choice(neightbors)
            for tile in self.board.getAllTiles():
                if(tile.getPosition()==newEmptyPosition):
                    tile.setPosition(self.board.getEmptyTile().getPosition())
                    self.board.swap(newEmptyPosition,self.board.getEmptyTile().getPosition())
                    self.board.getEmptyTile().setPosition(newEmptyPosition)
                    break;
        self.countShuffle+=1
        self.board.updateBoard()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.drawBoard()
        self.border.drawBorder()
        for button in self.buttons_list:
            button.draw(self.screen)
        Label(GAME_SIZE*TILESIZE+TILESIZE ,TILESIZE/2 , "%.3f" % self.elapsed_time).draw(self.screen)
        if(self.Mode==Mode.HUMAN_MODE):
            Label(GAME_SIZE*TILESIZE+TILESIZE ,TILESIZE,f"Total Step: {self.HumanResolver.totalSteps}" ).draw(self.screen)
        else:
            Label(GAME_SIZE*TILESIZE+TILESIZE ,TILESIZE,f"Total Step: {self.HumanResolver.totalSteps}" ).draw(self.screen)
        pygame.display.flip()


    def run(self):
        while True:
            # pygame.time.Clock().tick(FPS)
            self.draw()
            if self.Mode!=Mode.HUMAN_MODE and self.isPlaying:
                self.Algorithm.solve()
         
            if(self.isShuffle):
                self.shuffle()
                if self.Mode==Mode.HUMAN_MODE:
                    self.HumanResolver.totalSteps=0
                else:
                    self.Algorithm.setNewGame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if(self.Mode==Mode.SOLVER_MODE and self.isPlaying):
                    continue
                if(event.type==pygame.MOUSEBUTTONDOWN and not self.isShuffle):
                    mouse_x,mouse_y=pygame.mouse.get_pos()
                    for button in  self.buttons_list:
                        if button.click(mouse_x,mouse_y):
                            if button.text == "Shuffle":
                                self.shuffle()
                                self.isShuffle=True
                            elif button.text == "HUMAN-MODE":
                                self.HumanResolver=HumanSolver(self.board)
                                self.Mode=Mode.HUMAN_MODE
                            elif button.text =="DFS":
                                self.Algorithm=DFS(self.board)
                                self.Mode=Mode.SOLVER_MODE
                            elif button.text =="BFS":
                                self.Algorithm=BFS(self.board)
                                self.Mode=Mode.SOLVER_MODE
                            elif button.text =="A*":
                                self.Algorithm=AStar(self.board)
                                self.Mode=Mode.SOLVER_MODE
                            self.isPlaying=False
                            
                    if(self.Mode==Mode.HUMAN_MODE):
                        self.HumanResolver.click((mouse_x,mouse_y))
            
            if self.isPlaying :
                self.elapsed_time=time.time()-self.startTime
            elif not self.isPlaying and not self.board.isWin():
                self.elapsed_time=0
            if(self.isPlaying and self.board.isWin()):
                self.isPlaying=False
              


game = Game()
game.createGame()
game.run()