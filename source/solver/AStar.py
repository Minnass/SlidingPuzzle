from solver.Algorithm import*

from queue import PriorityQueue
class AStar(Algorithm):
    def __init__(self, gameBoard) -> None:
        super().__init__(gameBoard)
    def solve(self):
        if self.isFinished:
            self.move()
        else:
            #tinh dau tien
            original_f_heuristic=0
            for row in range(self.gameBoard.gameSiZe):
                for col in range(self.gameBoard.gameSiZe):
                    if self.gameBoard.currentGrids[row][col]==0:
                        continue
                    x_goalState=(self.gameBoard.currentGrids[row][col]-1)//self.gameBoard.gameSiZe
                    y_goalState=(self.gameBoard.currentGrids[row][col]-1)%self.gameBoard.gameSiZe
                    manhattanDistance=self.manhattanDistance((row,col),(x_goalState,y_goalState))
                    original_f_heuristic+=manhattanDistance
            open_list=PriorityQueue()
            explored_nodes=[]
            tmp_path=[]
            open_list.put((original_f_heuristic,self.gameBoard.currentGrids,self.gameBoard.getEmptyTile(
            ).getPosition(), self.gameBoard.getEmptyTile().getPosition()))
            while not open_list.empty():
                lastTuple = open_list.get()
                f_Heuristic_parent = lastTuple[0]
                parent_state=lastTuple[1]
                emptyTilePosition = lastTuple[2]
                swappedPosition = lastTuple[3]
                emptyTile = parent_state[emptyTilePosition[0]
                                         ][emptyTilePosition[1]]
                currentState = copy.deepcopy(parent_state)
                currentState[emptyTilePosition[0]][emptyTilePosition[1]
                                                   ] = currentState[swappedPosition[0]][swappedPosition[1]]
                currentState[swappedPosition[0]
                             ][swappedPosition[1]] = emptyTile                           
                # print('current state:',currentState)
                # print(f_Heuristic_parent)
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
                                break
                    self.isFinished=True
                    break
                # print('neighbor: ')    
                neighbors=self.getPossibleMove(swappedPosition)
                for neighbor in neighbors:
                    checked_stated = copy.deepcopy(currentState)
                    _temp = checked_stated[swappedPosition[0]
                                           ][swappedPosition[1]]
                    checked_stated[swappedPosition[0]][swappedPosition[1]
                                                       ] = checked_stated[neighbor[0]][neighbor[1]]
                    checked_stated[neighbor[0]][neighbor[1]] = _temp
                   
                    if checked_stated not in explored_nodes:
                        # print(checked_stated)
                        swappedValue=currentState[neighbor[0]][neighbor[1]]
                        x_swappedvalue_goalState=(swappedValue-1)//self.gameBoard.gameSiZe
                        y_swappedValue_goalState=(swappedValue-1)%self.gameBoard.gameSiZe
                        new_manhattanDistance=self.manhattanDistance(swappedPosition,(x_swappedvalue_goalState,y_swappedValue_goalState))
                        current_manhattanDistance=self.manhattanDistance(neighbor,(x_swappedvalue_goalState,y_swappedValue_goalState))
                        new_f_heuristic=f_Heuristic_parent-current_manhattanDistance+new_manhattanDistance
                        # print(new_f_heuristic)
                        explored_nodes.append(checked_stated)
                        open_list.put(
                            (new_f_heuristic,currentState, swappedPosition, neighbor))
                        tmp_path.append(
                            (swappedPosition, neighbor, checked_stated))             
    def manhattanDistance(self,originalState:tuple,nexState:tuple):
        return abs(originalState[0]-nexState[0])+abs(originalState[1]-nexState[1])
    


