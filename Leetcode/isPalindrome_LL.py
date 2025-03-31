class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    def reverse_ll(self, head):

        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev  

    def isPalindrome(self, head):
        if head is None or head.next is None:  
            return True

    
        slow = fast = head
        while fast and fast.next:  
            slow = slow.next
            fast = fast.next.next
        

        new_head = self.reverse_ll(slow)  


        first = head
        second = new_head
        while second: 
            if first.data != second.data:
                self.reverse_ll(new_head)  
                return False
            first = first.next
            second = second.next

        self.reverse_ll(new_head)
        return True


arr = [1, 2, 3, 2, 1] 
ll = Solution()
for i in arr:
    ll.insert(i)

print(ll.isPalindrome(ll.head)) 
