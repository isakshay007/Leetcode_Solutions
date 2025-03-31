from typing import Optional

class Node:
    def __init__(self, data=0, next=None, child=None):
        self.data = data
        self.next = next
        self.child = child

class Solution:

    def __init__(self):
        self.head = None

    def merge(self, list1: Node, list2: Node) -> Node:
        """Merges two sorted linked lists with child pointers."""
        dummyNode = Node(-1)
        res = dummyNode

        while list1 and list2:
            if list1.data < list2.data:
                res.child = list1
                list1 = list1.child
            else:
                res.child = list2
                list2 = list2.child
            res = res.child  

        if list1:
            res.child = list1
        if list2:
            res.child = list2

        return dummyNode.child  

    def flattenlist(self, head: Node) -> Node:
        """Recursively flattens the multi-level linked list."""
        if head is None or head.next is None:
            return head

        
        mergehead = self.flattenlist(head.next)

        
        head = self.merge(head, mergehead)

       
        head.next = None

        return head

    def printLinkedList(self, head: Node):
        """Prints the flattened linked list using child pointers."""
        while head:
            print(head.data, end=" -> " if head.child else "")
            head = head.child
        print()

    def printOriginalLinkedList(self, head: Node, depth=0):
        """Prints the original multi-level linked list with indentation."""
        while head:
            print(head.data, end="")

        
            if head.child:
                print(" -> ", end="")
                self.printOriginalLinkedList(head.child, depth + 1)

           
            if head.next:
                print()
                print("| " * depth, end="")
            head = head.next


head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

solution = Solution()
print("Original Multi-Level Linked List:")
solution.printOriginalLinkedList(head)
print("\n")

# Flattening the list
flattened_head = solution.flattenlist(head)

print("Flattened Linked List:")
solution.printLinkedList(flattened_head)
