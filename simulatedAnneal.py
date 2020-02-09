import random

def initialize(temperature):
    found = False
    numsLeft = list(range(1,20))
    random.shuffle(numsLeft)
    letterAssign = dict()
    for char, i in zip("abcdefghijklmnopqrs", range(19)):
        letterAssign[char] = numsLeft[i]
    sets = [['a','b','c'],['d','e','f','g'],['h','i','j','k','l'],['m','n','o','p']
        ,['q','r','s'],['h','m','q'],
        ['d','i','n','r'],['a','e','j','o','s'],
        ['b','f','k','p'],['c','g','l'],['l','p','s'],['g','k','o','r'],
        ['c','f','j','n','q'],['b','e','i','m'],['a','d','h']]
    startAnneal(temperature,lette, sets)
    
    found = check(letterAssign)
        
    print(letterAssign, numsLeft)

def startAnneal(temperature,letterAssign, sets):
    while temperature>0:
        possibleLetters = "abcdefghijklmnopqrs"
        random.shuffle(possibleLetters)
        letterOne = possibleLetters[0]
        letterTwo = possibleLetters[1]
        lettersCheck = False
        lettersCheck =partialCheck(lettersAssign, temperature, sets, letterOne, letterTwo) letterTwo)
        if check(lettersAssign):
            return( True, lettersAssign)
        else:
            Temperature -= .001



def check(letterAssign):

    checked = False
    for xset in sets:
        xsum = 0
        for char in xset:
            xsum += letterAssign[char]
        if xsum != 38:
            #print("failed",xsum)
            return(False)
    return(True)

def partialCheck(letterAssign, temperature, sets, letterOne, letterTwo):
    switch  = 1
    letterOneTrue = True
    letterTwoTrue = True
    for xset in set:
        xsum = 0
        for char in xset:
            xsum += lettersLeft[char]
            if Char == letterOneTrue:
                LetterOneTrue = ""
            elif Char == letterTwoTrue:
                LetterTwoTrue = "Maybe"
        if xsum == 38:
            if letterOneTrue == "Maybe":
                LetterOneTrue = True
            if letterTwoTrue == "Maybe":
                LetterTwo = True
    if letterTwo == 
                
    
    
    
    
            
simulatedAnneal()
