
from staticFunction import operationFunction, conditionFunction
import re

def parseInput(inputFile):

    checkCondition = lambda operand ,firstArgument, secondArgument : conditionFunction[operand](firstArgument, secondArgument)
    executeInstruction = lambda operand,firstArgument, secondArgument : operationFunction[operand](firstArgument, int(secondArgument))

    register = {}
    highScore = 0

    for instruction in inputFile:

        parameters = re.search(r'(.+)\s(.*)\s([+-]?\d+)\sif\s(.+)\s([<>!=]+)\s([+-]?\d+)', instruction)

        if parameters:
            #print("Next row")
            #print(parameters.group())

            checkRegister(parameters.group(4), register)

            if checkCondition(parameters.group(5), register[parameters.group(4)], int(parameters.group(6))):
                #print("Condition fulfiled")
                checkRegister(parameters.group(1), register)
                register[parameters.group(1)] = executeInstruction(parameters.group(2), register[parameters.group(1)], int(parameters.group(3)))
                if register[parameters.group(1)] > highScore:
                    highScore = register[parameters.group(1)]
                #print("Action executed. Dictionary: ", register)

            #else:
             #   print("Condition not fulfiled")

        else:
            print("Input file not in right format on line %s" % instruction)
    print("Biggest value was: ", highScore)
    return register


def checkRegister(variable, register):

    if variable not in register:
        register[variable] = 0

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return content.split('\n')


if __name__ == "__main__":

    inputFile = readFile('input.txt')

    register = parseInput(inputFile)

    print(register)

    print(max(register, key= register.get) , register[max(register, key= register.get)])

