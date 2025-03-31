from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        for index, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, index, lst))

        dummy = ListNode(-1)
        current = dummy

        while min_heap:
            val, index, node = heapq.heappop(min_heap) 
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next
