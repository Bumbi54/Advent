import sys
import math


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

if __name__ == "__main__":

    endLocation = int(sys.argv[1])

    calculateDistance(endLocation)


