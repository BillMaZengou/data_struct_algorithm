def listSum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

def listSumRecursion(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSumRecursion(numList[1:])

if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    print("Loop: {}; Recursion: {}".format(listSum(a), listSumRecursion(a)))
