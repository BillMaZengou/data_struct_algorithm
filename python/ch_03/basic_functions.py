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

class Node(object):
    """docstring for Node."""

    def __init__(self, initdata):
        super(Node, self).__init__()
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList(object):
    """docstring for UnorderedList."""

    def __init__(self):
        super(UnorderedList, self).__init__()
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.setNext())

    def append(self, item):
        total_length = self.length()
        current = self.head
        idx = 0
        while idx < total_length-1:
            current = current.getNext()
            idx += 1

        temp = Node(item)
        current.setNext(temp)

    def insert(self, item, toIdx):
        current = self.head
        previous = None
        idx = 0
        if toIdx == 0:
            self.add(item)
        else:
            while idx < toIdx:
                previous = current
                current = current.getNext()
                idx += 1

            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
        current = self.head
        found = False
        idx = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                idx += 1
        return idx

    def pop(self):
        total_length = self.length()
        current = self.head
        idx = 0
        while idx < total_length-2:
            current = current.getNext()
            idx += 1

        current.setNext(None)

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
    # d = Deque()
    # print(d.isEmpty())
    # d.addRear(4)
    # d.addRear("dog")
    # d.addFront("cat")
    # d.addFront(True)
    # print(d.size())
    # print(d.isEmpty())
    # d.addRear(8.4)
    # print(d.removeRear())
    # print(d.removeFront())

    """Node (for Linked List)"""
    # temp = Node(93)
    # print(temp.getData())
    # print(temp.getNext())

    """Unordered List"""
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(54)
    mylist.add(26)
    print(mylist.search(17))
    print(mylist.length())
    print("-"*10)
    current = mylist.head
    for i in range(mylist.length()):
         print(current.getData())
         current = current.getNext()

    print("-"*10)
    mylist.insert(12, 1)
    current = mylist.head
    for i in range(mylist.length()):
         print(current.getData())
         current = current.getNext()

    print("-"*10)
    mylist.append(13)
    current = mylist.head
    for i in range(mylist.length()):
         print(current.getData())
         current = current.getNext()

    print("-"*10)
    print(mylist.index(77))

    print("-"*10)
    mylist.pop()
    current = mylist.head
    for i in range(mylist.length()):
         print(current.getData())
         current = current.getNext()

if __name__ == '__main__':
    main()
