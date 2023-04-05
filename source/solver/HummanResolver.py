from solver import *
from ..GameSettings.Board import Board


class HumanSolver():
    def __init__(self, gameBoard: Board) -> None:
        self.gameBoard = gameBoard

    def click(self, mousePosition: tuple):
        neighbors = self.gameBoard.getNeighboringTilles()
        for position in neighbors:
            for tile in self.gameBoard.Tiles:
                if  tile.getPosition() == position and\
                    tile.getCoordinates()[0] <= mousePosition[0] <= tile.getCoordinates()[0]+self.gameBoard.gameSiZe and\
                    tile.getCoordinates()[1] <= mousePosition[1] <= tile.getCoordinates()[1]+self.gameBoard.gameSiZe:
                        _temp = self.gameBoard.getEmptyTile().getPosition()
                        self.gameBoard.getEmptyTile().setPosition(tile.getPosition())
                        tile.setPostion(_temp)
                        self.gameBoard.updateBoard()
                        return
                    
