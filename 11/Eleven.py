from operator import add
from direction import directions

def calculateNextStep(curentPostiton, nextStep):

    directionList = directions[nextStep]

    return list(map(add, curentPostiton, directionList))

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return  content.split(',')


if __name__ == "__main__":
    inputFile = readFile('input.txt')

    print(inputFile)
    maxLength = 0
    postion = [0, 0]
    for nextStep in inputFile:
        postion = calculateNextStep(postion, nextStep)
        maxLength = max(postion + [maxLength], key=abs)
    print(postion)
    print(maxLength)
