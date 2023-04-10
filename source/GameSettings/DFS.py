from Algorithm import *



class DFS(Algorithm):
    def __init__(self, gameBoard: Board) -> None:
        super().__init__(gameBoard)

    def solve(self):

        if self.isResolved():
            self.move()
       
        else:    
            open_list = []
            explored_nodes = []
            tmp_path=[]
            open_list.append((self.gameBoard.currentGrids, self.gameBoard.getEmptyTile(
            ).getPosition(), self.gameBoard.getEmptyTile().getPosition()))
            while  open_list:
                lastTuple=open_list.pop()
                parent_state=lastTuple[0]
                emptyTilePosition=lastTuple[1]
                swappedPosition=lastTuple[2]
                emptyTile=parent_state[emptyTilePosition[0]][emptyTilePosition[1]]
                currentState=copy.deepcopy(parent_state)
                currentState[emptyTilePosition[0]][emptyTilePosition[1]]=currentState[swappedPosition[0]][swappedPosition[1]]
                currentState[swappedPosition[0]][swappedPosition[1]]=emptyTile
                if(currentState  in explored_nodes):
                    continue
                explored_nodes.append(currentState)
                if(currentState==self.gameBoard.goalGrids):
                    iterator=self.gameBoard.goalGrids
                    while iterator!=self.gameBoard.currentGrids:
                        for i in tmp_path:
                             if i[2]==iterator:
                                firstPosition=i[0]
                                secondPosition= i[1]
                                previousState=copy.deepcopy(i[2])
                                _value=previousState[firstPosition[0]][firstPosition[1]]
                                previousState[firstPosition[0]][firstPosition[1]]=previousState[secondPosition[0]][secondPosition[1]]
                                previousState[secondPosition[0]][secondPosition[1]]=_value  
                                self.strategies.append((firstPosition,secondPosition))
                                self.steps+=1
                                iterator=previousState
                                break;     
                    self.isFinished=True  
                    break
                neighbors=self.getPossibleMove(swappedPosition)
                
                for neighbor in neighbors:
                    checked_stated=copy.deepcopy(currentState)
                    _temp=checked_stated[swappedPosition[0]][swappedPosition[1]]
                    checked_stated[swappedPosition[0]][swappedPosition[1]]=checked_stated[neighbor[0]][neighbor[1]]
                    checked_stated[neighbor[0]][neighbor[1]]=_temp
                  
                    if checked_stated not in explored_nodes:
                        open_list.append((currentState,swappedPosition,neighbor))
                        tmp_path.append((swappedPosition,neighbor,checked_stated))


   

