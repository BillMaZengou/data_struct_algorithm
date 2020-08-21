import sys
LIB_PATH = '../ch_03'
sys.path.append(LIB_PATH)
from basic_functions import Stack

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

def toStrStack(n, base, stack_history):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n%base])
        toStrStack(n//base, base, stack_history)

if __name__ == '__main__':
    print(toStr(10, 2))
    rStack = Stack()
    toStrStack(10, 2, rStack)
    while rStack.isEmpty() != True:
        print(rStack.pop(), end='')
    print()
    # print(rStack)
