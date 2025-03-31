class Solution:
    def reverse(self, stack):
        if not stack: 
            return
        
        top = stack.pop()  
        self.reverse(stack)  
        self.insertAtBottom(stack, top)  
    
    def insertAtBottom(self, stack, element):
        if not stack: 
            stack.append(element)
        else:
            temp = stack.pop()  
            self.insertAtBottom(stack, element)  
            stack.append(temp)  
solution = Solution()
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)
solution.reverse(stack)
print("Reversed Stack:", stack)
