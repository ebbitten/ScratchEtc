import itertools
import operator

def answer(food,grid):
    #initialize the input that we'll get all of the permutations of paths from
    N=len(grid)
    permInput=[]
    bestFood=-1
    #bestPath=""
    for i in range(N-1): #Will have 2*(n-1) total steps given a Grid of NxN starting in upper left, ending in lower right
        permInput.append([1,0])
        permInput.append([0,1])
    #now that we have all the possible paths that we could take lets walk through them
    bestFood=findBestPath(permInput,food,grid)
    if bestFood==500:
        bestFood=-1
    return bestFood
    
def findBestPath(permInput,food,grid):
    bestFood=500
    
    for path in itertools.permutations(permInput):
        foodLeft=food
        currentPos=[0,0]
        for step in path:
            currentPos=map(operator.add,currentPos,step)
            foodLeft=foodLeft-grid[currentPos[0]][currentPos[1]]
            if foodLeft<0:
                break
            elif foodLeft==0:
                return 0
        if 0<=foodLeft<bestFood:
            bestFood=foodLeft
    return bestFood
    
grid=[[0,2,5],[1,1,3],[2,1,1]]
food=12
x=answer(food,grid)