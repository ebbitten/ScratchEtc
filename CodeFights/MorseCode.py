def MorseCode(message, key):

    import collections
    originalDict={'A': '._',     'B': '_...',   'C': '_._.',
        'D': '_..',    'E': '.',      'F': '.._.',
        'G': '__.',    'H': '....',   'I': '..',
        'J': '.___',   'K': '_._',    'L': '._..',
        'M': '__',     'N': '_.',     'O': '___',
        'P': '.__.',   'Q': '__._',   'R': '._.',
     	'S': '...',    'T': '_',      'U': '.._',
        'V': '..._',   'W': '.__',    'X': '_.._',
        'Y': '_.__',   'Z': '__..',

        #'0': '_____',  '1': '.____',  '2': '..___',
        #'3': '...__',  '4': '...._',  '5': '.....',
        #'6': '_....',  '7': '__...',  '8': '___..',
        #'9': '____.'
    }
    newDict={}
    #format key
    originalKey=key
    key=[]
    for keys in originalKey.split(" "):
        key.append(keys)
    def findoffSet(key,originalDict):

        offset=0
        found = False
        startingString=collections.deque('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        while not found:
            # C is index 2 in the list, F is index 5 (counting from 0)
            if originalDict[startingString[2]]==key[0] and originalDict[startingString[5]]==key[1]:
                found = True
                return(offset)
            else:
                offset+=1
                startingString.rotate(-1)

    offset=findoffSet(key,originalDict)
    def makeNewDict(orignalDict,offset,newDict):
        startingString = collections.deque('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        startingString.rotate(-1*offset)
        normalString='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(normalString)):
            newDict[normalString[i]]=originalDict[startingString[i]]
    makeNewDict(originalDict,offset,newDict)
    #invert dictionary to allow lookup on morse code charater
    reverseDict={}
    for key,value in newDict.iteritems():
        reverseDict[value]=key
    #TODO make sure you're on 2.7
    messageTranslated=""
    words=message.split("  ")
    for word in words:
        chars=word.split(" ")
        for char in chars:
            messageTranslated+=reverseDict[char]
        messageTranslated+=" "
        #Add a space after each word
    #trim last space after last word
    messageTranslated=messageTranslated[0:len(messageTranslated)-1]
    print(messageTranslated)
    return(messageTranslated)