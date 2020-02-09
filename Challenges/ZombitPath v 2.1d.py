#import operator
def answer(food,grid):
    #initialize the input that we'll get all of the permutations of paths from
    N=len(grid)
    #if N>=20:
     #   return -1
    bestFood=201
    dir=[[0,1,0],[0,0,1]]
    growBranch=[[food,0,0]] #paths that need to have branches added
    #found=False
    while growBranch:
        branch=growBranch[-1] #try the most recently added branch
        if (branch[1]==(N-1) and branch[2]==(N-1)):
            if branch[0]<bestFood:
                bestFood=branch[0]
        else:
                for move in dir:
                    #check for both edge of grid, as well as foodLeft
                    aMove=[branch[0],branch[1]+move[1],branch[2]+move[2]]
                    #try evaluating all on one line and just have food at end to avoid indexError
                    if aMove[1]<N and aMove[2]<N:
                        aMove[0]=aMove[0]-grid[aMove[1]][aMove[2]]
                        if aMove[0]>=0:
                            growBranch.append(aMove)
        
        #liveBranch=list(growBranch)
        #growBranch=[]
        growBranch.remove(branch)
        #found=checkIfDone(growBranch,bestFood)
        if bestFood==0:
            break
    if bestFood==201:
        bestFood=-1
    return bestFood
    

#def spawnBranch(branch,dir,growBranch,grid,N):
##figure out a way to create new growBranches from the current live branch
#    for move in dir:
#        #check for both edge of grid, as well as foodLeft
#        aMove=[branch[0]+move[0],branch[1]+move[1],branch[2]+move[2]]
#        #try evaluating all on one line and just have food at end to avoid indexError
#        if aMove[1]<N and aMove[2]<N:
#            aMove[0]=aMove[0]-grid[aMove[1]][aMove[2]]
#            if aMove[0]>=0:
#                growBranch.append(aMove)
        
#def atEnd(branch,N):
##check to see if a branch is at the end of the grid    
#    if (branch[1]!=(N-1) or branch[2]!=(N-1)):
#        return False
#    else:
#        return True
    
#def checkIfDone(liveBranch,bestFood):
#    if not liveBranch:
#        found=True
#    elif bestFood==0:
#        found=True
#    else:
#        found=False
#    return found

#def findNextBranch(growBranch):
    #lets start by just trying to find branches with the least food left, currently putting in line
    #return min(growBranch)

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
