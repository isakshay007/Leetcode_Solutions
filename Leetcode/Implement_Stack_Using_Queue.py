from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()  # Main queue
        self.q2 = Queue()  # Temporary queue

    def push(self, x: int) -> None:
        self.q2.put(x)

        while not self.q1.empty():
            self.q2.put(self.q1.get())
        
        self.q1,self.q2 = self.q2,self.q1
         

    def pop(self) -> int:
        if self.q1.empty():
            return -1  # Stack is empty
        
        return self.q1.get()


    def top(self) -> int:
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()

# Example Usage:
myStack = MyStack()
myStack.push(1)
myStack.push(2)

print(myStack.top())   # Output: 2
print(myStack.pop())   # Output: 2
print(myStack.empty()) # Output: False
print(myStack.pop())   # Output: 1
print(myStack.empty()) # Output: True
