import random
import time
#from gtts import gTTS
#import os

choices = ['Economy', 'Economy', 'Economy', 'delux', 'delux', 'imperial']

def timedRun():
    print('Imperial', 'Economy', 'None', 'Economy', 'Delux', 'Economy', sep = '\n')
    for i in range(34):
        time.sleep(30)
        newChoice = random.choice(choices)
        if .15 > random.random():
            newChoice = 'None'
        print('order type of ' + newChoice + ' order number of ' + str(i+7))

def outerLoop():
    successfulRuns = 0
    for t in range(1000):
        if distributions():
            successfulRuns += 1
    print(successfulRuns/1000)

def distributions():
    Imperial = 1
    for i in range(34):
        newChoice = random.choice(choices)
        #print(newChoice)
        if newChoice == 'imperial':
            Imperial += 1
    if Imperial < 5:
        return False
    else:
        return True

timedRun()
