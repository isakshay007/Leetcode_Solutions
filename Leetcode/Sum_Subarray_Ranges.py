from typing import List

class Solution:
    def next_smaller_element(self, arr: List[int]) -> List[int]:
        n = len(arr)
        next_smaller = [n] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                idx = st.pop()
                next_smaller[idx] = i
            st.append(i)
        
        return next_smaller

    def prev_smaller_element(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prev_smaller = [-1] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                prev_smaller[i] = st[-1]
            st.append(i)
        
        return prev_smaller

    def next_larger_element(self, arr: List[int]) -> List[int]:
        n = len(arr)
        next_larger = [n] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                idx = st.pop()
                next_larger[idx] = i
            st.append(i)
        
        return next_larger

    def prev_larger_element(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prev_larger = [-1] * n
        st = []

        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            if st:
                prev_larger[i] = st[-1]
            st.append(i)
        
        return prev_larger

    def subArrayMin(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        next_smaller = self.next_smaller_element(arr)
        prev_smaller = self.prev_smaller_element(arr)

        total = 0
        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i
            total = (total + arr[i] * left_count * right_count) % MOD

        return total

    def subArrayMax(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        next_larger = self.next_larger_element(arr)
        prev_larger = self.prev_larger_element(arr)

        total = 0
        for i in range(n):
            left_count = i - prev_larger[i]
            right_count = next_larger[i] - i
            total = (total + arr[i] * left_count * right_count) % MOD

        return total

    def subArrayRanges(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        return (self.subArrayMax(nums) - self.subArrayMin(nums)) % MOD

# Test Cases
obj = Solution()
print(obj.subArrayRanges([1,2,3]))  # Expected output: 4
print(obj.subArrayRanges([1,3,3]))  # Expected output: 4
print(obj.subArrayRanges([4,-2,-3,4,1]))  # Expected output: 59
