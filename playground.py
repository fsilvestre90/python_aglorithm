from Stack import Stack

testStringValid = "(([{()}]))(([{()}]))"
testStringInvalid = "((){)}"
testStringUneven = "({[])"

def isCorrectCloser(peekedItem, currItem):
    if peekedItem == "(" and currItem == ")":
        return True
    elif peekedItem == "[" and currItem == "]":
        return True
    elif peekedItem == "{" and currItem == "}":
        return True

def isOpener(item):
    return item is "(" or item is "[" or item is "{"

def ProperlyClosed(incomingStr):
    # first check if input string is even, if not then exit
    if len(incomingStr) % 2 == 1:
        return False

    # init stuff
    stackOfOpeners = Stack()
    stringToCheck = list(incomingStr)

    # check each item in the string
    # if item is an opener, push in the stack
    # else check if next item is the closer of it
    for item in stringToCheck:
        if isOpener(item) is True:
            stackOfOpeners.Push(item)
        else:
            if isCorrectCloser(stackOfOpeners.Peek(), item):
                stackOfOpeners.Pop()

    if stackOfOpeners.Peek() is None:
        return True
    else:
        return False

print("Is your string properly closed, numbnuts? Answer: " + str(ProperlyClosed(testStringValid)))
print("Is your string properly closed, numbnuts? Answer: " + str(ProperlyClosed(testStringInvalid)))
print("Is your string properly closed, numbnuts? Answer: " + str(ProperlyClosed(testStringUneven)))
