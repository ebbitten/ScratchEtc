def rotateImage(a):
    n = len(a)
    for i in range(n//2):
        for j in range(i, (n - 1 - i)):
            currentCell = (i, j)
            currentCellValue = getValue(currentCell, a)
            for count in range(4):
                targetCell = rotate(currentCell, count, n, i)
                targetCellValue = getValue(targetCell, a)
                holdValue = targetCellValue
                setValue(targetCell, a, currentCellValue)
                currentCellValue = holdValue
                currentCell = targetCell
    return a


def rotate(cell, count, n, i):
    if count == 0:
        return ((cell[1], (n - 1 - i)))
    if count == 1:
        return (((n - 1 - i), (n - cell[0] - 1)))
    if count == 2:
        return ((cell[1], i))
    if count == 3:
        return ((i, n-cell[0]-1))


def getValue(cell, a):
    return (a[cell[0]][cell[1]])


def setValue(cell, a, value):
    a[cell[0]][cell[1]] = value

a = [[1,2,3], [4,5,6], [7,8,9]]
rotateImage(a)
print(a)
