import random

def outerLoop(trials, tolerance,lowerGuess, upperGuess,func, expectedOdds=0.500):
    currentOdds = 0
    calcTolerance = currentOdds - expectedOdds
    while abs(calcTolerance) > tolerance:
        K = (lowerGuess + upperGuess)/2
        currentOdds = innerLoop(trials, K, func)
        if currentOdds < expectedOdds:
            lowerGuess = K
        else:
            upperGuess = K
        calcTolerance = currentOdds - expectedOdds
        print("Current Upper bound",upperGuess,"Current Lower Bound",lowerGuess,
              "currentOdds",currentOdds,"K value",K,"CalcTolerance",calcTolerance)
    print("Final Answer", K)
        
    
def innerLoop(trials, K, func):
    totalWon = 0
    for t in range(trials):
        if func(K):
            totalWon += 1
    return (totalWon/trials)
        

def starWarsBattle(K):
    N = 9
    alive = True
    while (alive and N>0):
        for trooper in range(N):
            if random.random()<0.001:
                alive = False
        if random.random()<((K*N**.5)/1000):
            N -= 1
    if alive:
        return(True)
    else:
        return(False)

outerLoop(1000000, .001, 10, 200, starWarsBattle)
                
