from itertools import cycle
import time


def parseInput(inputFile):

    return [int(block) for block in inputFile.split('\t')]


def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        parsedContent = parseInput(content)
        return parsedContent

def calculateCycles(banks):

    configurationList = set()
    count = 0

    while True:

        maxBlock = max(enumerate(banks), key= lambda x : x[1])
        count += 1

        banks[maxBlock[0]] = 0

        for step in range(1, maxBlock[1] + 1):
            banks[(step + maxBlock[0]) % len(banks)] +=1

        if tuple(banks) in configurationList:
            break
        else:
            configurationList.add(tuple(banks))

    return count

def calculateCyclesInfinity(banks):

    configurationList = set()
    count = 0
    loopStartBank = None

    while True:

        maxBlock = max(enumerate(banks), key= lambda x : x[1])

        banks[maxBlock[0]] = 0

        for step in range(1, maxBlock[1] + 1):
            banks[(step + maxBlock[0]) % len(banks)] +=1

        if tuple(banks) == loopStartBank:
            break
        elif tuple(banks) in configurationList:
            count += 1
            if not loopStartBank:
                loopStartBank = tuple(banks)
        else:
            configurationList.add(tuple(banks))

    return count

if __name__ == "__main__":

    banks = readFile('input.txt')

    print(banks)

    #cyclesNumber = calculateCycles(banks)
    #print(cyclesNumber)

    cyclesNumberInfinity = calculateCyclesInfinity(banks)
    print(cyclesNumberInfinity)