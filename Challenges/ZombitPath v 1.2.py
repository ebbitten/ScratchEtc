import itertools
import operator

def answer(food,grid):
    #initialize the input that we'll get all of the permutations of paths from
    N=len(grid)
    permInput=[]
    #bestPath=""
    for i in range(N-1): #Will have 2*(n-1) total steps given a Grid of NxN starting in upper left, ending in lower right
        permInput.append([1,0])
        permInput.append([0,1])
    #now that we have all the possible paths that we could take lets walk through them
    x=list(itertools.permutations(permInput))
    x=set(x)
    bestFood=findBestPath(x,food,grid)
    if bestFood==500:
        bestFood=-1
    return bestFood
    
def findBestPath(permInput,food,grid):
    bestFood=500
    #consider checking diagonals to see if its even possible to cross first
    #also make sure break statements are working as intended 
    for path in itertools.chain(x):
        foodLeft=food
        currentPos=[0,0]
        for step in path:
            if foodLeft>=0:
                currentPos=map(operator.add,currentPos,step)
                foodLeft=foodLeft-grid[currentPos[0]][currentPos[1]]
            else:
                break 
        if 0<=foodLeft<bestFood:    
            bestFood=foodLeft
        if bestFood==0:
            break
    return bestFood
  
    
import random  
def genGrid(N):
    grid=[]
    for i in range(N):
        rowval=[]
        for j in range(N):
            cellval=random.randint(1,10)
            rowval.append(cellval)
        grid.append(rowval)
    grid[0][0]=0
    return grid
def genFood():
    return random.randint(1,200)
    

       
grid=[[0,2,5],[1,1,3],[2,1,1]]
food=12