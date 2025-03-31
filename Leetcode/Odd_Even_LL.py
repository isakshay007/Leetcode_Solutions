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

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even  

        while even and even.next:
            
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next

        odd.next = even_head  
        return head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


arr = [1, 2, 3, 4, 5]
ll = Solution()
for i in arr:
    ll.insert(i)

ll.head = ll.oddEvenList(ll.head)  
ll.display()
