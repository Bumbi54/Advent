listFunction = [lambda x: (x[0] + 1, x[1]), lambda x: (x[0], x[1] - 1), lambda x: (x[0] - 1, x[1]),
                lambda x: (x[0], x[1] + 1),
                lambda x: (x[0] + 1, x[1] + 1), lambda x: (x[0] - 1, x[1] - 1), lambda x: (x[0] + 1, x[1] - 1),
                lambda x: (x[0] - 1, x[1] + 1)]

listFunctionStep = [lambda x: (x[0], x[1] + 1), lambda x: (x[0] + 1, x[1] ), lambda x: (x[0], x[1] - 1),
                    lambda x: (x[0] - 1, x[1])]

currentFunction = [lambda x: (x[0], x[1] + 1)]