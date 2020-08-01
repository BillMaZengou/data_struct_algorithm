from basic_functions import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString

def main():
    print(baseConverter(10, 2))
    print(baseConverter(10, 16))
    print(baseConverter(10, 10))

if __name__ == '__main__':
    main()
