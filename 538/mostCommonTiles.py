import random
import operator

def outerLoop(length,trials):
    stable = False
    while not stable:
        oldStratList = stratList[:]
        stratList = findMostCommonSquares(
        print("Stratlist",stratList,"OldStratList",oldStratList)
        if stratList == oldStratList and "?" not in stratList:
            stable = True

def findMostCommonSquares(length,trials):
    curSquare = {}
    answerList = []
    for l in range(length):
        curSquare[l] = 0
    for t in range(trials):
        curPos = 0
        while curPos<length:
            curSquare[curPos] += 1
            curPos += random.choice([1,2,3,4,5,6])
    for l in range(length):
        answerList.append([l,curSquare[l]])
        answerSorted = sorted(answerList, key = operator.itemgetter(1), reverse=True)
    return(answerSorted[0:4])

findMostCommonSquares(1000,100000)
