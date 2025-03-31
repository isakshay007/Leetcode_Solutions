class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_val  = float('inf')

    def push(self, val:int)->None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        else:
            if val < self.min_val:
                self.stack.append(2*val-self.min_val)
                self.min_val = val
            else:
                self.stack.append(val)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top< self.min_val:
            self.min_val = 2*self.min_val-top

    def top(self):
        top = self.stack[-1]
        if top < self.min_val:
            return self.min_val
        return top
    
    def getMin(self):
        return self.min_val

min = MinStack()
print(min.push(2))