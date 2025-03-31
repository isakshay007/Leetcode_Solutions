from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = Counter(tasks)

        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)

        interval = 0 

        while max_heap:
            temp = []  
            for _ in range(n + 1):
                interval += 1  

                if max_heap:
                    count = heapq.heappop(max_heap)  
                    if count + 1 < 0:  
                        temp.append(count + 1)  

                if not max_heap and not temp:
                    break

            for count in temp:
                heapq.heappush(max_heap, count)

        return interval


tasks1 = ["A","A","A","B","B","B"]
n1 = 2
sol = Solution()
print(sol.leastInterval(tasks1, n1))  # Output: 8