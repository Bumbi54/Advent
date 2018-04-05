

def calculateSum(digits):
    digitsCircular = digits[:] + digits[:]

    print(digitsCircular)
    return sum(digits[index] for index in range(len(digits)) if digits[index] == digitsCircular[index+int(len(digits)/2)])


if __name__ == "__main__":

    digits = input("Enter list of digits: ")
    print(calculateSum([int(digit) for digit in str(digits)]))