from typing import List

class Solution:
    def next_smallest_element(self, arr: List[int]) -> List[int]:
        """Computes the Next Smaller Element (NSE) index for each element."""
        n = len(arr)
        next_smallest = [n] * n 
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smallest[idx] = i
            stack.append(i)
        return next_smallest

    def prev_smallest_element(self, arr: List[int]) -> List[int]:
        """Computes the Previous Smaller Element (PSE) index for each element."""
        n = len(arr)
        prev_smallest = [-1] * n 
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:  
                stack.pop()

            prev_smallest[i] = stack[-1] if stack else -1

            stack.append(i)
        return prev_smallest

    def sumSubarrayMins(self, arr: List[int]) -> int:
        """Calculates the sum of minimums in all subarrays."""
        n = len(arr)
        MOD = 10**9 + 7 

        next_smaller = self.next_smallest_element(arr)
        prev_smaller = self.prev_smallest_element(arr)

        total = 0
        for i in range(n):
            left_count = i - prev_smaller[i]  
            right_count = next_smaller[i] - i  

            total = (total + (left_count * right_count * arr[i])) % MOD

        return total


obj = Solution()
print(obj.sumSubarrayMins([3,1,2,4]))  # Output: 17
print(obj.sumSubarrayMins([11,81,94,43,3]))  # Output: 444
