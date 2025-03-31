from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        q = deque()  
        result = []

        for i in range(len(nums)):
            # Remove elements that are out of the window range
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Maintain decreasing order in deque, remove smaller elements
            while q and nums[q[-1]] < nums[i]:  # Fix: Ensure we remove smaller elements
                q.pop()

            # Add current element index
            q.append(i)

            # Store the max element once the window size reaches k
            if i >= k - 1:
                result.append(nums[q[0]])  # Fix: Append the actual max value, not the index

        return result

sol = Solution()
nums = [4, 0, -1, 3, 5, 3, 6, 8]
k = 3
print("Maximum element in every", k, "window:", sol.maxSlidingWindow(nums, k))
