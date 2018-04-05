import operator
from functools import reduce


def hashingFunction(hashList, inputLengths, currentPostion):

    skipSize = 0
    for step in inputLengths:

        subList = [hashList[(index + currentPostion) % len(hashList)]  for index in range(step)]

        reversedSubList = subList[::-1]

        for index, newElement in enumerate(reversedSubList):
            hashList[(currentPostion+index) % len(hashList)] = newElement
        currentPostion = (step + skipSize) % len(hashList) + currentPostion
        skipSize += 1

def hashingFunctionComplete(hashList, inputLengths, currentPostion, rounds):

    skipSize = 0
    for round in range(rounds):
        for step in inputLengths:

            subList = [hashList[(index + currentPostion) % len(hashList)]  for index in range(step)]

            reversedSubList = subList[::-1]

            for index, newElement in enumerate(reversedSubList):
                hashList[(currentPostion+index) % len(hashList)] = newElement
            currentPostion = (step + skipSize) % len(hashList) + currentPostion
            skipSize += 1

def denseHash(sparseHash, stepSize):

    subHashList = [sparseHash[step: (step + stepSize)]  for step in range(0,len(sparseHash), stepSize)]

    print(subHashList)

    return [reduce(operator.xor, subHash) for subHash in subHashList]
    #reduce(operator.xor, sparseHash)


def convertToHex(denseHashList):

    denseHashLisHex = [f"{digit:#0{4}x}" for digit in denseHashList]

    print(denseHashLisHex)

    #print(reduce(operator.add, denseHashLisHex))

    return ''.join(denseHashLisHex).replace('0x', '')

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return [int(step) for step in content.split(',')]


if __name__ == "__main__":

    inputFile = readFile('input.txt')

    startList = [value for value in range(256)]
    '''
    hashingFunction(startList, inputFile, currentPostion = 0)

    print(startList)
    print("Multiple: ", startList[0] * startList[1])
    '''
    hashingFunctionComplete(startList, inputFile, currentPostion = 0, rounds = 64)

    print(startList)

    denseHashList = denseHash(startList, stepSize = 16)

    print(denseHashList)

    finalHash = convertToHex(denseHashList)

    print("Final solution: ", finalHash, " With length: ", len(finalHash))






