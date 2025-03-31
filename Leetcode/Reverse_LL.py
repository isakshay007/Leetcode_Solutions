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

    def reverseList_Iterative(self):
        temp = self.head
        prev= None
        while temp:
            front  = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    
    def reverseList_recursive(self):
        if self.head is None or self.head.next is None:
            return None
        new_head = self.reverseList_recursive(self.head.next)
        front = self.head.next
        front.next = self.head
        self.head.next = None
        return new_head



arr = [1,2,3,4,5]
ll = Solution()
for i in arr:
    ll.insert(i)
ll.reverseList_recursive(ll.head) 

