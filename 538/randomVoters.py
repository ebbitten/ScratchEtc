import random
def randomVoters(nRangestart, nRangeEnd, trials,votingChance=.5):
    outArray=[]
    for n in range(nRangestart,nRangeEnd+1):
        outvalue=findChance(n, trials,votingChance)/trials
        outArray.append(outvalue)
    print(outArray)





def findChance(people, trials,votingchance):
    xsum=0
    for i in range(trials):
        cand1=0
        cand2=0
        #let's pretend we always want candidate 1
        for person in range(people):
            randvar=random.random()
            if randvar<=votingchance:
                cand1+=1
            else:
                cand2+=1
        if cand1==cand2 or cand1==cand2+1:
            xsum+=1
    return xsum

randomVoters(3619995,3619996, 10000,.5)
