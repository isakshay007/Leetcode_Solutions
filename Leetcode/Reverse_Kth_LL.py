from typing import Optional

class ListNode:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def reverseList_Iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKthNode(self, temp, k):
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None
        new_head = None

        while temp is not None:
            kThNode = self.getKthNode(temp, k)

            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kThNode.next
            kThNode.next = None

            reversed_head = self.reverseList_Iterative(temp)

            if new_head is None:
                new_head = reversed_head
            else:
                prevLast.next = reversed_head

            prevLast = temp
            temp = nextNode

        return new_head if new_head else head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


arr = [1,2,3,4,5,6,7,8,9,10]
ll = Solution()
for i in arr:
    ll.insert(i)


print("Original List:")
ll.display()

k = 3
ll.head = ll.reverseKGroup(ll.head, k)

print(f"Reversed List in Groups of {k}:")
ll.display()
