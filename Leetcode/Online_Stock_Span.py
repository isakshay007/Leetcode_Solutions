from typing import List
class StockSpanner:
    def __init__(self):
        self.stack=[]

    def next(self,price:int)->int:
        span = 1
        while self.stack and self.stack[-1][0]<=price:
            span = span + self.stack.pop()[1]
        self.stack.append((price,span))
        return span

# Example Usage
obj = StockSpanner()
print(obj.next(100))  # Output: 1
print(obj.next(80))   # Output: 1
print(obj.next(60))   # Output: 1
print(obj.next(70))   # Output: 2
