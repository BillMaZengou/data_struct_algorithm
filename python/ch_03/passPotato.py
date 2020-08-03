from basic_functions import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()  # return the last person's name

def main():
    survive = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    print(survive)

if __name__ == '__main__':
    main()
