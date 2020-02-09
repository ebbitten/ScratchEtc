import random

def tryToFind():
    found = False
    while not found:
        numsLeft = list(range(1,20))
        random.shuffle(numsLeft)
        lettersLeft = dict()
        for char, i in zip("abcdefghijklmnopqrs", range(19)):
            lettersLeft[char] = numsLeft[i]
        found = check(lettersLeft)
        
    print(lettersLeft, numsLeft)

def check(lettersLeft):
    sets = [['a','b','c'],['d','e','f','g'],['h','i','j','k','l'],['m','n','o','p']
            ,['q','r','s'],['h','m','q'],
            ['d','i','n','r'],['a','e','j','o','s'],
            ['b','f','k','p'],['c','g','l'],['l','p','s'],['g','k','o','r'],
            ['c','f','j','n','q'],['b','e','i','m'],['a','d','h']]
    checked = False
    for xset in sets:
        xsum = 0
        for char in xset:
            xsum += lettersLeft[char]
        if xsum != 38:
            #print("failed",xsum)
            return(False)
    return(True)
            
tryToFind()
