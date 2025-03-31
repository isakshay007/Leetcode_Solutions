class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currsize = 0
        self.maxsize = 16
        self.arr = [0]*self.maxsize
    
    def push(self,x):
        if self.currsize == self.maxsize:
            print("Queue is Full")
            exit(1)
        if self.end==-1:
            self.start=0
            self.end=0
        else:
            self.end = (self.end+1)%self.maxsize
        self.arr[self.end] = x
        self.currsize+=1

    def pop(self):
        if self.start==-1:
            print("Queue is empty")
        popped = self.arr[self.start]
        if self.currsize==1:
            self.start=-1
            self.end=-1
        else:
            self.start = (self.start+1)%self.maxsize
        self.currsize-=1
        return popped
    
    def top(self):
        if self.start==-1:
            print("Queue is empty")
            exit(1)
        return self.arr[self.start]
    
    def size(self):
        return self.currsize

if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())



