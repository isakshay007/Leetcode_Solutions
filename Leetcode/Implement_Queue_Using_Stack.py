class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2=[]
        

    def push(self, x: int) -> None:
        
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

        
    def pop(self) -> int:
        if not self.s1:
            return -1
        return self.s1.pop()
        

    def peek(self) -> int:
        if not self.s1:
            return -1
        return self.s1[-1]

    
    def empty(self) -> bool:
        return len(self.s1)==0

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)