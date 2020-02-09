import random

def outerLoop(steps = 20):
    stable = False
    stepList = [t/steps for t in range(0,steps+1)]
    stratList = ["?" for t in range(0,steps+1)]
    while not stable:
        oldStratList = stratList[:]
        for i in range(steps+1):
            strat = innerLoop(i, stratList,steps)
            stratList[i] = strat
        print("Stratlist",stratList,"OldStratList",oldStratList)
        if stratList == oldStratList and "?" not in stratList:
            stable = True
    
def innerLoop(i, stratList,steps):
    totalValueWar = 0
    totalValuePeace = 0
    #try peace
    for j in range(steps+1):
        myMove = "P"
        oppMove = stratList[j]
        totalValuePeace += battle(i, j, myMove, oppMove)
    #try war
    for j in range(steps+1):
        myMove = "W"
        oppMove = stratList[j]
        totalValueWar += battle(i, j, myMove, oppMove)
    if totalValueWar>totalValuePeace:
        return("W")
    elif totalValuePeace>totalValueWar:
        return("P")
    else:
        return("?")
        
        

def battle(myStr, oppStr, myMove, oppMove):
    if oppMove == "?":
        oppMove = random.choice(["P","W"])
    if myMove == "W" or oppMove == "W":
        if myStr>oppStr:
            return(2)
        else:
            return(0)
    else:
        return(1)

outerLoop()
                
