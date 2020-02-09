import itertools
import string
import math
def solution(n,c):
    #Initialize some variables
    nests=[]
    pathPos=[]
    connections=[]
    for i in range(n):
        nests.append((i,string.ascii_lowercase[i]))
    # compute how many maximum paths you could possibly take
    # also create a list of 0s and 1s twice as long as the list of paths
    maxPath=0
    for i in range(n):
        maxPath+=n
    for i in range(c):
        pathPos.append(1)
    for i in range(maxPath-c):
        pathPos.append(0)
    #create a permutation of above list p max path length
    perms=itertools.permutations(pathPos,maxPath)
    #iterate through those permutations assigning each 0 or 1 to a path
    for perm in perms:    #try each possible permutation
        connections=[]
        areConnected=False
        count=0
        sourceNum=n  #Start from the top for calculating but make thenactually start building the links from 0 up
        divisorSum=1 #This will be what we divide the position of the 1 or 0 by to find the destination nest
        for i in perm:
            if i and count<sourceNum:
                sourceNest=n-sourceNum
                destNest=count%divisorSum+(n-sourceNum+1)
                consolidateConnections(sourceNest,destNest,connections,n)
            count+=1
        #Think of a great way to map each 0 or 1 from the iterator to a connection between 2 nests that works as the number of nests grows
			#I think this will be something along the lines modulo using the the current position within the iterator and the number of nests
			#Modulo and floor division should provide the destination and source nest
        #for the first path you create add each of those nests to
        #for each additioanl path you create add it to the largest "connected" group, if it was part of other groups merge it

def consolidateConnections(source,dest,connections,n):
    if len(connections[0])==n:
        return(None) #If we already have all nests connected then bugger off
    sourceNum=0
    destNum=0
    sourceFound=False
    destFound=False
    for i in range(len(connections)):
        if source in connections[i]:
            sourceNum=i
            sourceFound=True
        if dest in connections[i]:
            destNum=i
            destFound=True
    if sourceNum==destNum:
        return(None)
    if not (sourceFound or destFound):
        connections.append([source,dest])
    if sourceFound and destFound:
        for i in connections[sourceNum]:
            connections[destNum].append(i)



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



solution(4,4)