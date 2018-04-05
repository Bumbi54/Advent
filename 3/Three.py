import sys
import math
from Functions import listFunction, listFunctionStep, currentFunction

def calculateDistance(endLocation):

    sizeOftable = math.ceil(math.sqrt(endLocation))
    firstValue = (sizeOftable - 1) * (sizeOftable - 1) + 1

    if not sizeOftable % 2:
        sizeOftable+=1
    else:
        firstValue-=1

    iteratorRow = sizeOftable
    iteratorColumn = sizeOftable

    maxValue = sizeOftable * sizeOftable

    print("In outer ring. End value: %s, first value: %s" % (maxValue, firstValue))

    for index in reversed(range(firstValue, maxValue+1)):
        print(index)

        if index == endLocation:
            print("Found postition: %s %s" %(iteratorRow, iteratorColumn))
            break

        if iteratorColumn != 1 and iteratorRow != 1 and iteratorRow == sizeOftable:
            print("Bottom row %s %s" % (iteratorRow, iteratorColumn))
            iteratorColumn-= 1

        elif iteratorColumn == 1 and iteratorRow != 1:
            print("Left row %s %s" % (iteratorRow, iteratorColumn))
            iteratorRow -= 1

        elif iteratorRow == 1 and iteratorColumn != sizeOftable:
            print("Top row %s %s" % (iteratorRow, iteratorColumn))
            iteratorColumn+= 1

        elif iteratorColumn == sizeOftable and iteratorRow != sizeOftable:
            print("Right row %s %s" % (iteratorRow, iteratorColumn))
            iteratorRow+= 1

    squareOne = math.ceil(sizeOftable/2)
    print("Location of square one: %s %s" % (squareOne, squareOne))

    distance = abs(iteratorColumn - squareOne) + abs(iteratorRow - squareOne)

    print("Distance from %s to square one is: %s" % (endLocation, distance))




def nextValue(dictMatrix, nextPosition):

    return sum(dictMatrix[function(nextPosition)] for function in listFunction if function(nextPosition) in dictMatrix)

def nextPosition(dictMatrix, previousPosition):

    next = [function for function in listFunctionStep if function(previousPosition) not in dictMatrix]

    if len(next) == 3:
        previous = [previousElement for previousElement in listFunctionStep if previousElement not in next][0]
        index = listFunctionStep.index(previous) + 1
        if index == len(listFunctionStep):
            index = 0
        currentFunction[0] = listFunctionStep[index]

    return currentFunction[0](previousPosition)


if __name__ == "__main__":

    input = int(sys.argv[1])

    dictMatrix = {(0, 0): 1, (0, 1) : 1}
    value = 1
    position = (0, 1)


    while value < input:
        position = nextPosition(dictMatrix, position)
        value = nextValue(dictMatrix, position)
        dictMatrix[position] = value
        print("Final value: %s " % value)
        print("Pozicija: ", position)
