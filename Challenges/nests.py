import itertools
import string
import math
def solution(n,c):
    #Initialize some variables
    nests=[]
    pathPos=[]
    connections=[]
    for i in n:
        nests.append(i,string.ascii_lowercase[i])
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
    for perm in perms:

        #Think of a great way to map each 0 or 1 from the iterator to a connection between 2 nests that works as the number of nests grows
			#I think this will be something along the lines modulo using the the current position within the iterator and the number of nests
			#Modulo and floor division should provide the destination and source nest
        #for the first path you create add each of those nests to
        #for each additioanl path you create add it to the largest "connected" group, if it was part of other groups merge it


def helperRec():
    pass