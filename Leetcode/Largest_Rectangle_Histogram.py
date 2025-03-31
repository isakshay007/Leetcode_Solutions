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

    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = self.prev_smaller_element(heights)
        nse = self.next_smaller_element(heights)
        maximum = 0
        n = len(heights)
        for i in range(n):
            maximum  = max(maximum,heights[i]*(nse[i]-pse[i]-1))
        return maximum
    
obj = Solution()
print(obj.largestRectangleArea([2,1,5,6,2,3])) 