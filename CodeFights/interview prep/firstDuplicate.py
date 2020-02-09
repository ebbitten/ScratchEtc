def firstDuplicate(a):

    seen = []
    for i, ele in enumerate(a):
        if ele in seen:
            return(i)
        else:
            seen.append(ele)
    return(-1)

a = [2, 3, 3, 1, 5, 2]

print(firstDuplicate(a))
