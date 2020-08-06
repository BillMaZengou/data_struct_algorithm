# Palindrome problem is to detect if a word is a palindrome.
# palindrome is word like "radar", "toot"

from basic_functions import Deque

def palChecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

def main():
    print(palChecker("lsdkjfskf"))
    print(palChecker("toot"))

if __name__ == '__main__':
    main()
