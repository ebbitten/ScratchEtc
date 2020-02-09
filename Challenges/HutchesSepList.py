import bisect

def answer(heights):
    totalWater=0
    #Populate walls list by checking to see if each hutch would trap water
    numHutches=len(heights)
    #really might want to switch to dicts, or even a list of dicts
    lWallH=[-1] #populating so that max can be evaluated
    lWallP=[-1]
    rWallH=[-1] #populating so that max can be evaluated
    rWallP=[numHutches]

    #Let's first get a list of every hutch that can ask as a "left wall"
    for i in range(0,numHutches-1):
        #print(heights[i],heights[i+1],max(lWalls),max(lWalls, key=lambda x: x[1])[1])
        if (heights[i]>heights[i+1] and heights[i]>max(lWallH)):
            lWallP.append(i)
            lWallH.append(heights[i])
    #for right walls we'll do same thing just in reverse
    for i in range(numHutches-1,0,-1):
        if (heights[i]>heights[i-1] and heights[i]>max(rWallH)):
            rWallP.append(i)
            rWallH.append(heights[i])
    print(lWallP)
    print(lWallH)
    print(rWallP)
    print(rWallH)


    #now let's loop over each hutch (except the ends) to see how much water they'll hold
    leftWall=-1
    rightWall=-1
    for i in range(1,numHutches-1):
        #find left wall
        for wall in lWallP:
            if wall>i:
                break #not working as intended
            wallI=wall
        wallIndex=lWallP.index(wallI)
        leftWall=lWallH[wallIndex] #want to find one before, because the last one tested caused it to break
        #find right wall
        for wall in rWallP:
            if i>wall:
                break
            wallI=wall
        wallIndex=rWallP.index(wallI)
        rightWall=rWallH[wallIndex]
        effWallH=min(rightWall,leftWall)
        waterHdiff=max(0,effWallH-heights[i])
        totalWater+=waterHdiff
    return totalWater
                          
heights=[1, 4, 2, 5, 1, 2, 3]
x=answer(heights)
