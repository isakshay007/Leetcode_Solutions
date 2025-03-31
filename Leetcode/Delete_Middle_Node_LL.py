from typing import Optional
class ListNode:
    def __init__(self,data1=0,next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_Node = ListNode(data)
        if self.head is None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_Node

   
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next.next if head.next else None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

arr = [1,2,3,4,5]
ll= Solution()
for i in arr:
    ll.insert(i)
ll.deleteMiddle(ll.head)
ll.display()
