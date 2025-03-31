class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1
class Solution:
    def __init__(self):
        self.head = None

    def Length_Loop(self,head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = fast.next
                loop_len = 1
                while slow != fast:
                    fast = fast.next
                    loop_len+=1
                return loop_len
        return 0


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  


solution = Solution()
cycle_length = solution.Length_Loop(head)
if cycle_length:
    print(cycle_length)
else:
    print("No")