import sys
import re

def cleanText(fileContent):
    print(fileContent)

    withoutExclamationMark = re.sub(r"(!.?)",r"", fileContent)
    print(withoutExclamationMark)

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



if __name__ == "__main__":

    file = open(sys.argv[1], "r")

    cleanText(file.readline())

