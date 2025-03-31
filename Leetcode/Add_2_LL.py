from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        """ Inserts a new node at the end of the linked list. """
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Adds two numbers represented as linked lists and returns a new linked list. """
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            temp.next = ListNode(sum%10)
            temp = temp.next
        return dummy.next

    def display(self, node: Optional[ListNode]):
        """ Prints the linked list starting from the given node. """
        temp = node
        while temp:
            print(temp.val, end=" -> " if temp.next else "")
            temp = temp.next
        print()


l1 = Solution()
for i in [0, 9]:
    l1.insert(i)

l2 = Solution()
for i in [1, 0]:
    l2.insert(i)

print("First Linked List:")
l1.display(l1.head)

print("Second Linked List:")
l2.display(l2.head)

result = Solution().addTwoNumbers(l1.head, l2.head)

print("Resultant Linked List:")
Solution().display(result)
