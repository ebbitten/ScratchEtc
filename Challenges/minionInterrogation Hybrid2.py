def answer(minions):
    import math
    answerList=[]
    minionList=[]
    conf=.2

    #This part definitely is useful
    #
    for i in range(len(minions)):
        tempList=[]
        percentage=minions[i][1]/float(minions[i][2])
        timeIndex=round((math.log(conf)/math.log(1-percentage)),0)*minions[i][0] #round to represent discreteness
        timeIndex2=(percentage)/(minions[i][0]) #also factor in
        for j in range(1000):
            tempList.append([i,0,percentage,minions[i][0]])
        timeIndex3=time(tempList)
        minionList.append([i,timeIndex,percentage,minions[i][0],timeIndex2,timeIndex3])
    from operator import itemgetter
    #testing out weighted average
    print(minionList)
    minionList1=sorted(minionList, key = itemgetter(1))
    for i in range(len(minions)):
        minionList1[i][1]=float(i)*0
    #print(minionList)
    minionList2=sorted(minionList, key = itemgetter(4),reverse=True)
    for i in range(len(minions)):
        minionList2[i][1]+=float(i)*1
    minionList3=sorted(minionList, key = itemgetter(5))
    for i in range(len(minions)):
        minionList3[i][1]+=float(i)*1
    #print(minionList)
    minionList=sorted(minionList, key=itemgetter(1))
    #print(minionList)

 
    
    #I don't think this part actually does anything
    #
    minionListFinal=minionList[:]
    minTime=time(minionList)
    #print("Initial minTime= "+str(minTime))
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

   #  This function works I'm pretty sure...
    #
def time(minionList):
    stillGoing=1
    timeTaken=0
    for i in range(len(minionList)):
        timeTaken+=minionList[i][3]*stillGoing
        stillGoing*=(1-minionList[i][2])
    return timeTaken
