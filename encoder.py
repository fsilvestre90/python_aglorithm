from random import randint


def IntEncoderToString(integerToConvert, base):
    digits = "0123456789ABCDEF"
    # init a stack to store remainders
    binaryStack = []

    # perform division on incoming integer, saving the remainder
    # push the remainder into the stack
    while integerToConvert > 0:
        remainder = integerToConvert % base
        binaryStack.append(remainder)
        integerToConvert = integerToConvert // base

    # take stack values and convert to binary String
    outputString = ""
    while len(binaryStack) is not 0:
        outputString += digits[binaryStack.pop()]
    return outputString

def StringDecoderToInt():
    outputInt = 0
    return outputInt

# test functions
randInt = randint(0,255)
print("Integer to convert: " + str(randInt))
print("Converted Value: " + IntEncoderToString(randInt, 16))
