def answer(t, n):
    #outside function to initialize memoization, t is how many rolls, n is how long
    endPos=n
    
    rollsLeft=t
    mem = {}
    def recurFind(rollsLeft, position):
        # Number of ways to get from p to n in exactly t rolls, modulo m.
        index = rollsLeft, position
        #If we've already cached the result, then use it
        if index in mem:
            return mem[index]
        #If we're at the end, or if we only have enough moves to get to the end then return "1"
        elif position < 1 or rollsLeft < endPos - position:
            return 0
        elif position == endPos or rollsLeft == endPos - position:
            return 1
        #If we've moved off the board (to the left) or if we don't have enough moves to get to the end then return 0

        else:
            rollsLeft-=1

            result = (recurFind(rollsLeft, position - 1) + recurFind(rollsLeft, position) + recurFind(rollsLeft, position + 1)) % 123454321
            mem[index] = result
            return result
    return recurFind(rollsLeft, 1)


print(answer(3,2))
