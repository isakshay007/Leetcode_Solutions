class Queue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, x):
        element = self.QueueNode(x)
        if self.start is None:
            self.start = self.end = element
        else:
            self.end.next = element
            self.end = element
        self.size += 1       

    def pop(self):
        if self.start is None:
            return -1 
        temp = self.start
        self.start = self.start.next 
        self.size -= 1
        return temp.data  

    def top(self):
        if self.start is None:
            return -1  
        return self.start.data  

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def printQueue(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    q = Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    q.printQueue()  # Output: 10 20 30

 
