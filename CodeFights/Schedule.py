import itertools

monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekDayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def recurringTask(firstDate, k, daysOfTheWeek, n):
    answer = []
    calcDate = firstDate
    cycleCount=0
    dayscounted=0
    # print('hi')
    for i in range(n):
        # print(calcDate, 'hi')  # print date and add it to our list
        answer.append(calcDate)
        # store off current dates
        day = int(calcDate[0:2])
        month = int(calcDate[3:5])
        year = int(calcDate[6:10])
        # figure out current day of week
        dayofWeek = findDay(day, month, year)
        # figure out next day of week
        foundDay = False
        foundNextDay = False
        for dayCycle in itertools.cycle(weekDayNames):
            print(dayCycle)
            if not foundDay:
                if dayCycle == dayofWeek:
                    foundDay = True
                    print('Found original day',dayofWeek)
            else:
                if dayCycle in daysOfTheWeek:
                    foundNextDay = dayCycle
                    print('Found nextDay',foundNextDay)
                    break
        # figure out how much we need to progress
        nextDayIndex = weekDayNames.index(foundNextDay)
        dayofWeekIndex = weekDayNames.index(dayofWeek)
        days_2_progress = nextDayIndex - dayofWeekIndex
        print(dayofWeek,foundNextDay,days_2_progress)
        if 1 > days_2_progress:
            days_2_progress += 7
        dayscounted+=1
        if dayscounted==len(daysOfTheWeek):
            cycleCount+=1
            while cycleCount<k:
                days_2_progress +=7
                cycleCount+=1
            cycleCount=0
        currentDays = computeDaysElapsed(day, month, year)
        newDays = currentDays + days_2_progress
        calcDate = findDate(newDays)
    return (answer)


def findDay(day, month, year):
    '''finds the day of the week given a day, month, year in integers
    Keeping in mind that date starts on 1/1/1900 which is a Monday'''
    daysElapsed = computeDaysElapsed(day, month, year)
    dayOffset = daysElapsed % 7
    if dayOffset == 6:
        dayOffset = -1  # Cycle starts on Sunday, but 1/1/1900 was a Monday
    dayofWeek = weekDayNames[1 + dayOffset]
    return(dayofWeek)


def computeDaysElapsed(day, month, year):
    daysElapsed = 0
    for i in range(year - 1900):
        if i % 4 == 0 and ((i%400==0 and i%100==0) or i%100!=0):
            daysElapsed += 366
        else:
            daysElapsed += 365
    for i in range(month-1): #don't actually want to go through the month you're in
        daysElapsed += monthLengths[i]
    if year % 4 == 0 and not ((year%400==0 and year%100==0) or (year%100!=0)) and (month > 2):
        daysElapsed += 1
    for i in range(day-1): #don't actually want to go through the day you're in
        daysElapsed += 1
    return (daysElapsed)


def findDate(totalDays):
    year = 1900
    month = 1
    day = 1
    # find how many years we get forward
    daystoChop = 365
    while totalDays >= daystoChop:
        year += 1
        totalDays -= daystoChop
        daystoChop = 365
        if year % 4 == 0:
            daystoChop = 366
        if not ((year%400==0 and year%100==0) or (year%100!=0)):
            daystoChop=365
    daystoChop = monthLengths[0]
    while totalDays >= daystoChop:
        month += 1
        totalDays -= daystoChop
        if month<=11:
            daystoChop = monthLengths[month-1]
            if month==2 and year%4==0 and ((year%400==0 and year%100==0) or (year%100!=0)):
                daystoChop=29
        else:
            daystoChop=31
    while totalDays > 0:
        day += 1
        totalDays -= 1
    year = str(year)
    month = str(month)
    day = str(day)
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day
    calcDate =day  + "/" + month + "/" + year
    return (calcDate)



firstDate= "01/02/2100"
k= 4
daysOfTheWeek= ["Sunday", 
 "Monday"]
n= 4
recurringTask(firstDate,k,daysOfTheWeek,n)
