from Tile import*

class Board():
    def __init__(self,game,gameSize) -> None:
        self.all_sprites=game.all_sprites
        self.gameSiZe=gameSize
        self.sourceGrids=[]
        self.goalGrids=[]
        self.Tiles=[]
    
    def createBoard(self):
        
        for row in range(1,1+self.gameSiZe):
            self.sourceGrids.append([])
            self.goalGrids.append([])
            for col in range(1,1+self.gameSiZe):
                self.sourceGrids[row-1].append((row-1)*self.gameSiZe+col)
                self.goalGrids[row-1].append((row-1)*self.gameSiZe+col)
        self.sourceGrids[-1][-1]=0
        self.goalGrids[-1][-1]=0
        
        for row in range(self.gameSiZe):
            for col in range(self.gameSiZe):
                self.Tiles.append(Tile(row,col,self.TileImages[row*self.gameSiZe+col],self.all_sprites))
    def drawBoard(self):
        self.all_sprites.draw()            
    def shuffle(self):
        pass
    def setTileImages(self,paths):
        self.TileImages=paths
    def isFinishGame(self):
        if(self.sourceGrids==self.goalGrids):
            return True
        else: 
            return False
        
        
a=[[1,2,3],[4,5,6],[7,8,0]]
b=[[1,2,3],[4,5,6],[7,8,0]]
if(a==b):
    print('True')
else:
    print('false')