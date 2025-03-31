from typing import Optional

class ListNode:
    def __init__(self, data1=0, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, head: Optional[ListNode], data: int) -> ListNode:
        """
        Inserts a node at the end of the linked list and returns the head.
        """
        new_Node = ListNode(data)
        if head is None:
            return new_Node
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_Node
        return head

    def collisionPoint(self, t1: ListNode, t2: ListNode, d: int) -> Optional[ListNode]:

        while d:
            t2 = t2.next
            d -= 1
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
        return t1  

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1, temp2 = headA, headB
        n1, n2 = 0, 0

        while temp1:
            n1 += 1
            temp1 = temp1.next


        while temp2:
            n2 += 1
            temp2 = temp2.next

        if n1 < n2:
            return self.collisionPoint(headA, headB, n2 - n1)
        else:
            return self.collisionPoint(headB, headA, n1 - n2)

    def display(self, head: Optional[ListNode]):

        temp = head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


ll = Solution()


head = None
head = ll.insert(head, 1)
head = ll.insert(head, 3)
head = ll.insert(head, 1)
head = ll.insert(head, 2)
head = ll.insert(head, 4)
head1 = head 
head = head.next.next.next  

headSec = None
headSec = ll.insert(headSec, 3)
head2 = headSec  
headSec.next = head  

print("List 1:")
ll.display(head1)
print("List 2:")
ll.display(head2)

intersection_node = ll.getIntersectionNode(head1, head2)
if intersection_node:
    print("Intersection at node with value:", intersection_node.data)
else:
    print("No intersection found.")
