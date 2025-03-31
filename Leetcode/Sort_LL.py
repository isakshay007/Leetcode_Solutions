from typing import Optional

class ListNode:
    def __init__(self, data1=0, next1=None):
        
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
    
    def mergeTwoSortedLinkedLists(self, list1, list2):  
        
        dummyNode = ListNode(-1)
        temp = dummyNode

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
    
        return dummyNode.next

    def middleNode(self, head): 
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        middle = self.middleNode(head)
        right = middle.next
        left = head
        middle.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoSortedLinkedLists(left, right) 

    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

arr = [4, 2, 1, 5, 3]  
ll = Solution()
for i in arr:
    ll.insert(i)

print("Before Sorting:")
ll.display()

ll.head = ll.sortList(ll.head)  

print("After Sorting:")
ll.display()
