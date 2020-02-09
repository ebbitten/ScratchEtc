def processText(inputFilePath,outputFilePath,*speakers):
    f = open(inputFilePath,'r')
    currentSpeaker=""
    speakerDict={}
    speakerCount={}
    for speaker in speakers:
        speakerDict[speaker]=set()
        speakerCount[speaker]=0
    for line in f:
        currentSpeaker=processLine(line,speakerDict,speakerCount,currentSpeaker)
    f.close()
    speakerWords={}
    for speaker in speakerDict.keys():
        speakerWords[speaker]=len(speakerDict[speaker])
    saveText=""
    for speaker in speakerWords:
        saveText+='Speaker'+str(speaker)+' said '+str(speakerWords[speaker])+' unique words'
        saveText+='\n'
        saveText+='Speaker'+str(speaker)+' said '+str(speakerCount[speaker])+' total words'
        saveText+='\n'
    f = open(outputFilePath,'w')
    f.write(saveText)
    f.close()


def processLine(line,speakerDict,speakerCount,currentSpeaker):
    for word in line.split():
        if word in speakerDict.keys():
            currentSpeaker=word
        else:
            speakerDict[currentSpeaker].add(word.upper())
            speakerCount[currentSpeaker]+=1
    return currentSpeaker

processText('First debate text.txt','First debate processed','TRUMP:','HOLT:','CLINTON:')


