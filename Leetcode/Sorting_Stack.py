
class Solution:
    def sort(self, stack):
        if len(stack) <= 1:
            return
        
        top = stack.pop()  
        self.sort(stack)   
        self.insert(stack, top)  
    
    def insert(self, stack, element):
        if not stack or element > stack[-1]:  
            stack.append(element)
        else:
            temp = stack.pop()  
            self.insert(stack, element)  
            stack.append(temp) 

# Example Usage
solution = Solution()
stack = [11, 2, 32, 3, 41]
solution.sort(stack)
print(stack)  
