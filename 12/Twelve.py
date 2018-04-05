import re

def calculatePaths(inputFile):

    pathDictionary = {}
    for row in inputFile.split('\n'):
        print(row)
        m = re.search(r'(.*) <-> (.*)', row)
        if m:
            print(m.group(1))
            print(m.group(2))

def addPath():

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return  content

if __name__ == "__main__":
    inputFile = readFile('input.txt')

    calculatePaths(inputFile)