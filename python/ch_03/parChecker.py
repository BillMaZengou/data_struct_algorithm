from basic_functions import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def main():
    print(parChecker("(()()()())"))
    print(parChecker("(((((())))))"))
    print(parChecker("((((((((())"))

if __name__ == '__main__':
    main()
