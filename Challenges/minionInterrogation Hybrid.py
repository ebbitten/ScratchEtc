minions=[[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
def answer(minions):
    import math
    answerList=[]
    minionList=[]
    conf=.2

    #This part definitely is useful
    #
    for i in range(len(minions)):
        percentage=minions[i][1]/float(minions[i][2])
        timeIndex=round((math.log(conf)/math.log(1-percentage)),0)*minions[i][0] #round to represent discreteness
        timeIndex2=(1-percentage)*(minions[i][0]) #also factor in 
        minionList.append([i,timeIndex,percentage,minions[i][0],timeIndex2])
    from operator import itemgetter
    #testing out weighted average
    print(minionList)
    minionList1=sorted(minionList, key = itemgetter(1))
    for i in range(len(minions)):
        minionList1[i][1]=i
    print(minionList)
    minionList2=sorted(minionList, key = itemgetter(4))
    for i in range(len(minions)):
        minionList2[i][1]+=float(i)
    print(minionList)
    minionList=sorted(minionList, key=itemgetter(1))
    print(minionList)

    #  This function works I'm pretty sure...
    #
    

    #I don't think this part actually does anything
    #
    minionListFinal=minionList[:]
    minTime=time(minionList)
    print("Initial minTime= "+str(minTime))
    for i in minionList:
        minionListCopy=minionList[:]
        last=i
        minionListCopy.remove(i)
        minionListCopy.append(last)
        #print minionListCopy
        timeCheck=time(minionListCopy)
        #print("timeCheck= "+str(timeCheck))
        if timeCheck<=minTime:
            if minionListFinal>minionListCopy[:]:
                minTime=timeCheck
                #print(minionListFinal)
                #print(minionListCopy)
                minionListFinal=minionListCopy[:]

    #This is definitely important           
    for i in minionListFinal:
        answerList.append(i[0])
    return answerList

def time(minionList):
    stillGoing=1
    timeTaken=0
    for i in range(len(minionList)):
        timeTaken+=minionList[i][3]*stillGoing
        stillGoing*=(1-minionList[i][2])
    return timeTaken

x=answer(minions)

