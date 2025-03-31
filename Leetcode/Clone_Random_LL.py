from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """Creates a deep copy of a linked list with random pointers."""
        if not head:
            return None

        # Step 1: Insert copied nodes next to original nodes
        temp = head
        while temp:
            new_node = Node(temp.val, temp.next, None)
            temp.next = new_node
            temp = new_node.next

        # Step 2: Assign random pointers to copied nodes
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Step 3: Extract copied list while restoring original list
        original = head
        copied = head.next
        copied_head = copied  

        while original:
            original.next = copied.next
            original = original.next
            if copied.next:
                copied.next = copied.next.next
                copied = copied.next

        return copied_head  

    def printLinkedList(self, head: Optional[Node]):
        """Prints the linked list with random pointers."""
        while head:
            random_val = head.random.val if head.random else "None"
            print(f"Val: {head.val}, Random: {random_val}")
            head = head.next

# Example Usage
if __name__ == "__main__":
   
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    solution = Solution()
    print("Original Linked List with Random Pointers:")
    solution.printLinkedList(head)

    cloned_list = solution.copyRandomList(head)

    print("\nCloned Linked List with Random Pointers:")
    solution.printLinkedList(cloned_list)
