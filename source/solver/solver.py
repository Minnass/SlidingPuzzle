from abc import ABC,abstractmethod
class Solver(ABC):
    def __init__(self,gameBoard) -> None:
        self.gameBoard=self.gameBoard
    @abstractmethod
    def solve(self):
        pass    
    
