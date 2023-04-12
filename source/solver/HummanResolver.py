from GameSettings.Board import Board
from GameSettings.settings import *

class HumanSolver():
    def __init__(self, gameBoard: Board) -> None:
        self.gameBoard = gameBoard
        self.totalSteps=0

    def click(self, mousePosition: tuple):
        neighbors = self.gameBoard.getNeighboringTilles()
        for position in neighbors:
            for tile in self.gameBoard.getAllTiles():

                if  tile.getPosition() == position and\
                    tile.getCoordinates()[0] <= mousePosition[1] <= tile.getCoordinates()[0]+TILESIZE and\
                    tile.getCoordinates()[1] <= mousePosition[0] <= tile.getCoordinates()[1]+TILESIZE:
                        _temp = self.gameBoard.getEmptyTile().getPosition()
                        self.gameBoard.swap(_temp,tile.getPosition())
                        self.gameBoard.getEmptyTile().setPosition(tile.getPosition())
                        tile.setPosition(_temp)
                        self.totalSteps+=1
                        self.gameBoard.updateBoard()
                        return
    def getTotalStep(self):
        return self.totalSteps
                    
