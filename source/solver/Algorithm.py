from GameSettings.Board import *
from abc import ABC, abstractmethod
import copy
import time
class Algorithm():
    def __init__(self, gameBoard: Board) -> None:
        self.steps = 0
        self.isFinished=False
        self.gameBoard = gameBoard
        self.strategies = []

    @abstractmethod
    def solve(self):
        # do something here
        pass

    def setStep(self, number):
        self.steps = number

    def getPossibleMove(self, emptyPostion: tuple):
     
        up = (emptyPostion[0]-1, emptyPostion[1]
              ) if emptyPostion[0]-1 >= 0 else None
        down = (emptyPostion[0]+1, emptyPostion[1]
                ) if emptyPostion[0]+1 < self.gameBoard.gameSiZe else None
        left = (emptyPostion[0], emptyPostion[1] -
                1) if emptyPostion[1]-1 >= 0 else None
        right = (emptyPostion[0], emptyPostion[1] +
                 1) if emptyPostion[1]+1 < self.gameBoard.gameSiZe else None

        directions = [up,left, down, right]
        neighbors = []
        for dir in directions:
            if dir is not None:
                neighbors.append(dir)
      
        return neighbors
    def isResolved(self):
        return True if self.isFinished is True else False
    def move(self):
        firstPosition,secondPosition=move_direction=self.strategies.pop()
        self.gameBoard.swap(firstPosition,secondPosition)
        for tile in self.gameBoard.getAllTiles():
            if tile.getPosition()==secondPosition:
                tile.setPosition(firstPosition)
                self.gameBoard.getEmptyTile().setPosition(secondPosition)
                break;
        self.gameBoard.updateBoard()
        time.sleep(1.1)
    
    def setNewGame(self):
        self.isFinished=False
        self.steps=0
    
