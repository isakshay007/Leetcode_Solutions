class Stack:
    class StackNode:
        def __init__(self,data):
            self.data = data
            self.next =  None
    
    def __init__(self):
        self.top = None
        self.size = 0

    def stack_push(self,x):
        element = self.StackNode(x)
        element.next = self.top
        self.top=  element
        self.size+=1

    def stack_pop(self):
        if self.top is None:
            return -1
        top_data = self.top.data
        self.top = self.top.next
        self.size-=1
        return top_data
    
    def size(self):
        return self.size
    
    def print(self):
        temp = self.top
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    s = Stack()
    s.stack_push(10)
    s.stack_push(20)
    s.print()

            
