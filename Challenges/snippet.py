def answer(document, searchTerms):
    searchTerms=[' '+word+' ' for word in searchTerms]
    words=document.split()
    currentStartPos=0
    bestLength=len(words)
    bestStartPos=0
    startedAtWord=False
    currentPos=0
    #consider turning searchTerms into set if it looks like they give me repeating ones
    while currentPos<len(words):
        toFind=list(searchTerms)
        currentPos=currentStartPos
        foundFirstWord=False
        #search for all the terms
        while toFind:
            if str(' '+words[currentPos]+' ') in toFind:
                toFind.remove(' '+words[currentPos]+' ')
                #take note of where we find the first word
                if not foundFirstWord:
                    firstWordLoc=currentPos
                    foundFirstWord=True
            else:
                currentPos+=1
                if currentPos>=len(words):
                    break
        #figure out how far that was
        length=currentPos-currentStartPos+1
        if length<bestLength:
            bestLength=length
            bestStartPos=currentStartPos
        #if we started at where we found the first word last time then let's increment one from there
        if startedAtWord:
            currentStartPos+=1
            startedAtWord=False
        #otherwise lets start at where we found the first word
        else:
            currentStartPos=firstWordLoc
            startedAtWord=True
    #gather the answer (consider redoing the string so that all words have spaces
    answerx=""
    value=str(words[bestStartPos]+' ')
    answerx+=value
    for i in range(bestLength-2):
        value=str(words[bestStartPos+i+1]+' ')
        answerx+=value
    value=str(words[bestStartPos+bestLength-1])
    answerx+=value
    return answerx
        
document='many google employees can program'
searchTerms=['google', 'program']
x=answer(document,searchTerms)
        
