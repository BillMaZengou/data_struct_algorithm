class Stack(object):
    """docstring for Stack."""

    def __init__(self):
        super(Stack, self).__init__()
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue(object):
    """docstring for Queue."""

    def __init__(self):
        super(Queue, self).__init__()
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque(object):
    """docstring for Deque."""

    def __init__(self):
        super(Deque, self).__init__()
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def main():
    """Stack"""
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())

    """Queue"""
    # q = Queue()
    # print(q.isEmpty())
    # q.enqueue(4)
    # q.enqueue('dog')
    # q.enqueue(True)
    # print(q.size())
    # print(q.isEmpty())
    # q.enqueue(8.4)
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.size())

    """Deque"""
    d = Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear("dog")
    d.addFront("cat")
    d.addFront(True)
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())

if __name__ == '__main__':
    main()
