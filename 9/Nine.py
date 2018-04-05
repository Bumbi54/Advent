import sys
import re

def cleanText(fileContent):
    print(fileContent)

    withoutExclamationMark = re.sub(r"(!.?)",r"", fileContent)
    print(withoutExclamationMark)

    countGarbage(withoutExclamationMark)

    withoutGarbage = re.sub(r"(<.*?>)",r"", withoutExclamationMark)
    print(withoutGarbage)

    totalScore = 0
    multiplier = 1

    for i in range(len(withoutGarbage)):

        if withoutGarbage[i] == '{':
            totalScore+= multiplier
            multiplier+= 1

        elif withoutGarbage[i] == '}':
            multiplier-= 1

    print("This is number of all groups: %s" % totalScore)

def countGarbage(partiallyCleanedFileContent):

    garbage = re.findall(r"<(.*?)>", partiallyCleanedFileContent)

    count = sum([len(element) for element in garbage])
    print("Number of garbage items: ", count)

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return content


if __name__ == "__main__":

    file = readFile('dump.txt')

    cleanText(file)

