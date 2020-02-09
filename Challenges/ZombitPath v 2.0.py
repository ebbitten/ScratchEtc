    #lets try constructing dynamically
import itertools
import operator
    
def answer(food,grid):
    #initialize the input that we'll get all of the permutations of paths from
    N=len(grid)
    bestFood=500
    directions=[[0,1,0],[0,0,1]]
    growingBranch=[[food,0,0]] #paths that need to have branches added
    found=False
    while not found:
        branch=findNextBranch(growingBranch)
        if atEnd(branch,N):
            if 0<=branch[0]<bestFood:
                bestFood=branch[0]
        else:
            spawnBranch(branch,directions,growingBranch,grid,N)
        #liveBranch=list(growingBranch)
        #growingBranch=[]
        growingBranch.remove(branch)
        found=checkIfDone(growingBranch,bestFood)
    if bestFood==500:
        bestFood=-1
    return bestFood
    

def spawnBranch(branch,directions,growingBranch,grid,N):
#figure out a way to create new growingBranches from the current live branch
    for move in directions:
        #check for both edge of grid, as well as foodLeft
        attmptMove=[branch[0]+move[0],branch[1]+move[1],branch[2]+move[2]]
        #try evaluating all on one line and just have food at end to avoid indexError
        if attmptMove[1]<N and attmptMove[2]<N and grid[attmptMove[0]][attmptMove[1]]<=attmptMove[0]:
            attmptMove[0]=attmptMove[0]-grid[attmptMove[0]][attmptMove[1]]
            growingBranch.append(attmptMove)
        
def atEnd(branch,N):
#check to see if a branch is at the end of the grid    
    if (branch[0]==(N-1) and branch[1]==(N-1)):
        return True
    else:
        return False
    
def checkIfDone(growingBranch,bestFood):
    if not growingBranch:
        found=True
    elif bestFood==0:
        found=True
    else:
        found=False
    return found

def findNextBranch(growingBranch):
    #lets start by just trying to find branches with the least food left
    return min(growingBranch)
        
    
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
food= 12
print(answer(food,grid))


#check if there are still liveBranches or if we found one that gets us there with 0 food left


#def findBestPath(permInput,food,grid):
#    bestFood=500
#    #consider checking diagonals to see if its even possible to cross first
#    #also make sure break statements are working as intended 
#    for path in itertools.chain(x):
#        foodLeft=food
#        currentPos=[0,0]
#        for step in path:
#            if foodLeft>=0:
#                currentPos=map(operator.add,currentPos,step)
#                foodLeft=foodLeft-grid[currentPos[0]][currentPos[1]]
#            else:
#                break 
#        if 0<=foodLeft<bestFood:    
#            bestFood=foodLeft
#        if bestFood==0:
#            break
#    return bestFood
  
    
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
    

