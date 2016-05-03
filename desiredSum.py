# Given list of numbers and desired sum, return if 3 numbers of that list sum is the desired value

def containsSum(inputList, Q):
    possibleValues = {}

    # cut list down by calculating all the partial sums
    # add to dictionary if they are under  the
    for key in inputList:
        # print("Key {}".format(inputList[key]))
        firstFactor = inputList[key]
        try:
            secondFactor = inputList[key+1]
            thirdFactor = inputList[key+2]
        except IndexError:
            break

        partialSum = firstFactor + secondFactor

        # if the partial sum is equal to Q, exit
        if partialSum == Q:
            return True

        # if partial sum is less than Q, add the third factor
        # if that is true, exit
        # else add it to the possible sum dictionary
        if partialSum <= Q:
            totalSum = partialSum + thirdFactor
            if totalSum == Q :
                return True
            else:
                for key in possibleValues:
                    if possibleValues[key] != firstFactor or possibleValues[key] != secondFactor:
                        possibleValues[firstFactor] = 1
                        possibleValues[secondFactor] = 1

    print(possibleValues)

    if len(possibleValues) > 3:
        containsSum(possibleValues, Q)
    else:
        return False

list =  [3, 5, 6, 7, 8, 9, 13, 15, 17]
# 3, 8, 17 = 28
# 15, 17, 3 = 35

sum = 35

print(containsSum(list, sum))