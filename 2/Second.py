
def openFile(fileName):
    with open(fileName, "r") as file:
        return [row.split( ) for row in file.read().split('\n')]

def calculatechecksum(inputList):
    print(inputList)
    return sum((int(max(row, key=int)) - int(min(row, key=int))) for row in inputList)

def calculateDivisibleValues(inputList):
    print(inputList)
    return sum(int(divided) / int(deviter)  for row in inputList for divided in row for deviter in row if int(divided) % int(deviter) == 0 and  divided != deviter)



if __name__ == "__main__":
    print(calculateDivisibleValues(openFile("input.txt")))

