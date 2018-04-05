

def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return content


def exitMaze(maze):

    step = 0
    i = 0

    while True:
        if step >= len(maze):
            print("Exit after %s steps" % i)
            break
        currentStep = step
        step += maze[step]
        if maze[currentStep] >= 3:
            maze[currentStep] -= 1
        else:
            maze[currentStep] += 1
        i += 1


if __name__ == "__main__":

    fileName = 'input.txt'

    maze = readFile(fileName)
    print(maze.split('\n'))
    #alternative : list(map(int, list))
    converToInt = lambda stringList : [int(element) for element in stringList]

    exitMaze(converToInt(maze.split('\n')))

