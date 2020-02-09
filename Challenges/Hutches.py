import bisect

def answer(heights):
    #Populate walls list by checking to see if each hutch would trap water
    numHutches=len(heights)
    lWalls=[[-1,-1]] #populating so that max can be evaluated
    rWalls=[[numHutches,-1]] #populating so that max can be evaluated
    

    #Let's first get a list of every hutch that can ask as a "left wall"
    for i in range(0,numHutches-1):
        #print(heights[i],heights[i+1],max(lWalls),max(lWalls, key=lambda x: x[1])[1])
        if (heights[i]>heights[i+1] and heights[i]>max(lWalls, key=lambda x: x[1])[1]):
            lWalls.append([i,heights[i]])
    #for right walls we'll do same thing just in reverse
    for i in range(numHutches-1,0,-1):
        print(i)
        if (heights[i]>heights[i-1] and heights[i]>max(rWalls, key=lambda x: x[1])[1]):
            rWalls.append([i,heights[i]])
    #print(rWalls)
    print(lWalls)

    #now let's loop over each hutch (except the ends) to see how much water they'll hold
    leftWall=0
    rightWall=0
    lWallsI=[x[0] for x in lWalls]
    print(lWallsI)
    rWallsI=rWalls[0]
    for i in range(1,numHutches-1):
        leftWallI=bisect.bisect_right(lWallsI,i)
        leftWall
        print(leftWall)
                          
heights=[1, 4, 2, 5, 1, 2, 3]
answer(heights)
