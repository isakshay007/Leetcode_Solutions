from typing import Optional

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            if fast.next:
                fast = fast.next

        if not fast.next:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

   
        slow.next = slow.next.next if slow.next else None
        
        return dummy.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


arr = [1, 2, 3, 4, 5]
n = 2
ll = Solution()
for i in arr:
    ll.insert(i)

ll.head = ll.removeNthFromEnd(ll.head, n)  
ll.display()
