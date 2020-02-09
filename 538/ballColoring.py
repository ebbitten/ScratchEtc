import random

def outerLoop(trials):
    total = 0
    for i in range(trials):
        total += ballRun()
    avg = total/trials
    print("The average number per trial was ",avg)

def ballRun():
    balls = ['b','g','r','y']
    index = [0,1,2,3]
    ballsSame = False
    counter = 0
    while not ballsSame:
        counter += 1
        copyindex = index[:]
        firstChoice =random.choice(copyindex)
        copyindex.remove(firstChoice)
        secondChoice = random.choice(copyindex)
        balls[secondChoice] = balls[firstChoice]
        if(all(x==balls[0] for x in balls)):
            ballsSame = True
    return counter


outerLoop(10000)
