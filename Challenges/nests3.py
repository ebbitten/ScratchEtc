import itertools
import string
import math
def answer(N,K):
    #Initialize some variables
    n=N
    c=K
    if K==N-1:
        return(int(n**(n-2)))

    nests=[]
    pathPos=[]
    connections=[]
    for i in range(n):
        nests.append((i,string.ascii_lowercase[i]))
    # compute how many maximum paths you could possibly take
    # also create a list of 0s and 1s twice as long as the list of paths
    maxPath=0
    for i in range(n):
        maxPath+=i
    if k==maxPath:
        return(1)

    for i in range(c):
        pathPos.append(1)
    for i in range(maxPath-c):
        pathPos.append(0)
    #create a permutation of above list p max path length
    #print(pathPos)
    perms=perm_unique(pathPos)
    #print(perms)
    total=0
    #iterate through those permutations assigning each 0 or 1 to a path
    for perm in perms:    #try each possible permutation
        connections=[]
        areConnected=False
        count=0
        sourceNum=n  #Start from the top for calculating but make thenactually start building the links from 0 up
        sourceNest=n-sourceNum
        destNest=1
        # divisorSum=1 #This will be what we divide the position of the 1 or 0 by to find the destination nest
        print('perm is',perm)
        for i in perm:
            if i:
                areConnected=consolidateConnections(sourceNest,destNest,connections,n)
                print('connections are', connections,'perm is', perm,'source, dest',sourceNest,destNest)
            if areConnected:
                break
            if destNest+1<n: #+1 because your index starts at 0, but n is the number of nests
                destNest+=1
            else:
                sourceNest+=1
                destNest=sourceNest+1
        if len(connections[0])==n:
            areConnected=True
        if areConnected:
            total+=1
        #Think of a great way to map each 0 or 1 from the iterator to a connection between 2 nests that works as the number of nests grows
			#I think this will be something along the lines modulo using the the current position within the iterator and the number of nests
			#Modulo and floor division should provide the destination and source nest
        #for the first path you create add each of those nests to
        #for each additioanl path you create add it to the largest "connected" group, if it was part of other groups merge it
        print(areConnected)
    return(total)

def consolidateConnections(source,dest,connections,n):
    if not connections:
        connections.append([source, dest])
    if len(connections[0])==n:
        return(True) #If we already have all nests connected then bugger off
    sourceNum=-1
    destNum=-1
    sourceFound=False
    destFound=False
    for i in range(len(connections)):
        if source in connections[i]:
            sourceNum=i
            sourceFound=True
            # #print('source',i,source)
        if dest in connections[i]:
            destNum=i
            destFound=True
            # #print('dest',i,dest)
    if not (sourceFound or destFound):
        connections.append([source,dest])
    if sourceNum==destNum:
        #print(sourceNum,destNum)
        return(False)
    if (sourceFound and destFound):
        for i in connections[sourceNum]:
            connections[destNum].append(i)
        del connections[sourceNum]
    elif sourceFound:
        #print(connections[sourceNum],dest)
        connections[sourceNum].append(dest)
    elif destFound:
        connections[destNum].append(source)
    return(False)



class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)

def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in perm_unique_helper(listunique, result_list, d - 1):
                    yield g
                i.occurrences += 1

import time
import timeit
print('solution is', answer(4,3))
# startTime=time.time()
# call=answer(3,2)
# endTime=time.time()
# print('Start time',startTime,'end time',endTime,'time diff',endTime-startTime)
# print(timeit.timeit(call))
