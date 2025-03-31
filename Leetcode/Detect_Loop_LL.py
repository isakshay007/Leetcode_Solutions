class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node 
    
    def hasCycle(self) -> bool:
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def hasCycle_Start(self):
        slow=fast=self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
    
arr=[1,2,3,4,5,6,7,8,9,3]
ll = Solution()
for i in arr:
    ll.insert(i)
ll.hasCycle()
