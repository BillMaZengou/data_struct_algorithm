from basic_functions import Queue
import random

class Printer(object):
    """docstring for Printer."""

    def __init__(self, ppm):
        super(Printer, self).__init__()
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60/self.pagerate

class Task(object):
    """docstring for Task."""

    def __init__(self, time, taskPageRange):
        super(Task, self).__init__()
        self.timestamp = time
        self.pages = random.randrange(1, taskPageRange+1)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

def simulation(numSeconds, pagesPerMinute, taskPageRange=20):
    lab_printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waiting_times = []

    for current_second in range(numSeconds):
        if newPrintTask():
            task = Task(current_second, taskPageRange)
            printQueue.enqueue(task)

        if (not lab_printer.busy()) and (not printQueue.isEmpty()):
            next_task = printQueue.dequeue()
            waiting_times.append(next_task.waitTime(current_second))
            lab_printer.startNext(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def main():
    pagesPerMinute = 3
    print("print %d per minute" % pagesPerMinute)
    for i in range(10):
        simulation(3600, pagesPerMinute)
    print("-"*40)

    pagesPerMinute = 10
    print("print %d per minute" % pagesPerMinute)
    for i in range(10):
        simulation(3600, pagesPerMinute)
    print("-"*40)

    pagesPerMinute = 5
    num_of_student = 20
    print("print %d per minute, number of student is %d" % (pagesPerMinute, num_of_student))
    for i in range(num_of_student):
        simulation(3600, pagesPerMinute)
    print("-"*40)

    pagesPerMinute = 5
    num_of_student = 10
    print("print %d per minute, number of student is %d" % (pagesPerMinute, num_of_student))
    for i in range(num_of_student):
        simulation(3600, pagesPerMinute, taskPageRange=10)

if __name__ == '__main__':
    main()
