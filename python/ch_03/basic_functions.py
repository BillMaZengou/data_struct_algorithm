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

def main():
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

    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

if __name__ == '__main__':
    main()
