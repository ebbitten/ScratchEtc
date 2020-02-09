def closestSequence(a, b):
    bestDiff = -1
    maskBound = 1 << len(b)

    for mask in range(maskBound):
        diff = 0
        curPos = 0
        for i in range(len(b)):
            if (mask & (1 << i)) != 0:
                diff += abs(a[curPos] - b[i])
                curPos += 1
                if curPos == len(a):
                    break
        if (mask&(sum([x**2 for x in range(len(a))]))==(sum([x**2 for x in range(len(a))]))) and (bestDiff == -1 or diff < bestDiff):
            bestDiff = diff

    return bestDiff


a=[1,2,6]
b=[0,1,3,4,5]
print(closestSequence(a,b))
