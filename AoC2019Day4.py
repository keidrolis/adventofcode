# Advent of Code 2019 day 4


def Check_Part_Two(numString):
    # print(numString)

    if not (numString[0] <= numString[1] and numString[1] <= numString[2] and numString[2] <= numString[3] and numString[3] <= numString[4] and numString[4] <= numString[5]):
        return False

    if (numString[0] == numString[1] and numString[1] != numString[2]):
        return True

    if (numString[1] == numString[2] and numString[2] != numString[3] and numString[1] != numString[0]):
        return True

    if (numString[2] == numString[3] and numString[3] != numString[4] and numString[2] != numString[1]):
        return True

    if (numString[3] == numString[4] and numString[4] != numString[5] and numString[3] != numString[2]):
        return True

    if (numString[4] == numString[5] and numString[4] != numString[3]):
        return True

    return False


startNumber = 372304
endNumber = 847060
possibleAnswers = []

currentNumber = startNumber

while currentNumber <= endNumber:
    numString = str(currentNumber)
    if Check_Part_Two(numString) == True:
        possibleAnswers.append(currentNumber)

    currentNumber += 1

print(len(possibleAnswers))

# print(Check_Part_Two(str(123444)))

print(possibleAnswers)
