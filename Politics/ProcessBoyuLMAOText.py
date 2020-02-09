def processText(inputFilePath,outputFilePath):
    f = open(inputFilePath,'r')
    speakerArray=[]
    curDate=""
    position=0
    lastLmaoDate=""
    for line in f:
        curDate,position,lastLmaoDate=processLine(line,speakerArray,curDate,position,lastLmaoDate)
    f.close()
    saveText=""
    for index in speakerArray:
        saveText+=str(index[0])+","+str(index[1])
        saveText+='\n'
    f = open(outputFilePath,'w')
    f.write(saveText)
    f.close()


def processLine(line,speakerArray,curDate,position,lastLmaoDate):
    piece=0
    sameDate=False #Figure out if this is the same date
    for part in line.split(","):
        if piece==0 and part!='18605603559':
            return curDate,position, lastLmaoDate
        elif piece==1:
            if part==lastLmaoDate:
                sameDate=True
            date=part
        elif piece!=0:
            for word in part.split():
                if word.upper()=="lmao".upper():
                    lastLmaoDate=date
                    if sameDate:
                        speakerArray[position-1][1]+=1
                    else:
                        speakerArray.append([str(date+'"'), 1])
                        position+=1
        piece+=1
    return date,position,lastLmaoDate

processText('Texts.csv','BoyuProcessed.txt')


