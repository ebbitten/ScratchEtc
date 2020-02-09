import operator
def answer(food,grid):
    #initialize the input that we'll get all of the permutations of paths from
    N=len(grid)
    #if N>=20:
     #   return -1
    bestFood=201
    directions=[[0,1,0],[0,0,1]]
    growingBranch=[[food,0,0]] #paths that need to have branches added
    found=False
    while not found:
        branch=findNextBranch(growingBranch)
        if atEnd(branch,N):
            if branch[0]<bestFood:
                bestFood=branch[0]
        else:
            spawnBranch(branch,directions,growingBranch,grid,N)
        #liveBranch=list(growingBranch)
        #growingBranch=[]
        growingBranch.remove(branch)
        found=checkIfDone(growingBranch,bestFood)
    if bestFood==201:
        bestFood=-1
    return bestFood
    

def spawnBranch(branch,directions,growingBranch,grid,N):
#figure out a way to create new growingBranches from the current live branch
    for move in directions:
        #check for both edge of grid, as well as foodLeft
        attmptMove=[branch[0]+move[0],branch[1]+move[1],branch[2]+move[2]]
        #try evaluating all on one line and just have food at end to avoid indexError
        if attmptMove[1]<N and attmptMove[2]<N and grid[attmptMove[1]][attmptMove[2]]<=attmptMove[0]:
            attmptMove[0]=attmptMove[0]-grid[attmptMove[1]][attmptMove[2]]
            growingBranch.append(attmptMove)
        
def atEnd(branch,N):
#check to see if a branch is at the end of the grid    
    if (branch[1]==(N-1) and branch[2]==(N-1)):
        return True
    else:
        return False
    
def checkIfDone(liveBranch,bestFood):
    if not liveBranch:
        found=True
    elif bestFood==0:
        found=True
    else:
        found=False
    return found

def findNextBranch(growingBranch):
    #lets start by just trying to find branches with the least food left
    return min(growingBranch)

grid=[[0, 8, 6, 8, 7, 8, 7],
 [10, 2, 8, 3, 3, 2, 8],
 [2, 9, 1, 6, 9, 9, 2],
 [3, 8, 10, 2, 7, 8, 1],
 [4, 4, 9, 7, 6, 10, 8],
 [6, 10, 7, 8, 6, 1, 1],
 [10, 1, 3, 2, 9, 2, 5]]
 
food=150

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