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

    def firstNthNode(self, temp: ListNode, target_position: int) -> ListNode:
        cnt = 1
        while temp:
            if cnt == target_position:
                return temp
            cnt += 1
            temp = temp.next
        return None  

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next: 
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        tail.next = head

        new_last_node = self.firstNthNode(head, length - k)

        new_head = new_last_node.next
        new_last_node.next = None

        return new_head  
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

arr = [1, 2, 3, 4, 5]
k = 2
ll = Solution()
for i in arr:
    ll.insert(i)

print("Original Linked List:")
ll.display()

ll.head = ll.rotateRight(ll.head, k)

print("Rotated Linked List:")
ll.display()
