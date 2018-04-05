import re

class Tower:

    def __init__(self, ID, value, children):
        self.ID = ID
        self.value = int(value)
        self.parent = None
        if children[0]:
            self.children = children
        else:
            self.children = None

def parseInput(inputFile):
    towers = {}

    for row in inputFile.split('\n'):

        m = re.search(r'(.*) \((\d+)\)(\s?-?>?\s?(.*))?', row)

        if m:
            towers[m.group(1)] = Tower(m.group(1), m.group(2), m.group(4).split(', '))
        else:
            print('Input file in wrong format on row: ', row)
            break

    return towers

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        parsedContent = parseInput(content)
        return parsedContent


def makeTree(regularDictinary):

    for tower in regularDictinary.values():
        if tower.children:
            for child in tower.children:
                regularDictinary[child].parent = tower
                tower.children = [regularDictinary[child] if parentChild == child else parentChild for parentChild in tower.children]

def findRoot(regularDictinary):

    return [tower for tower in regularDictinary.values() if not tower.parent][0]

def calculateWeight(tower, weight):

    if not tower.children:
        return weight

    childrenWeight = [calculateWeight(child, child.value) for child in tower.children if tower.children]

    if childrenWeight.count(childrenWeight[0]) != len(childrenWeight):
        print("Problem in children of: ", tower.ID)
        calculateWrongValue(tower.children, childrenWeight)

    return sum(childrenWeight) + weight

def calculateWrongValue(children, childrenWeight):

    print("Problem children list:", childrenWeight)
    problemChild = min([(child, childrenWeight.count(calculateWeight(child, child.value))) for child in children ], key= lambda x : x[1])

    print("ID and Value of wrong tower:",problemChild[0].ID, problemChild[0].value)
    print("Possible fixes: ", childrenWeight[0] - childrenWeight[-1] )


if __name__ == "__main__":

    inputFile = readFile('input.txt')

    makeTree(inputFile)

    rootTower = findRoot(inputFile)

    print(rootTower.ID)

    calculateWeight(rootTower, rootTower.value)
