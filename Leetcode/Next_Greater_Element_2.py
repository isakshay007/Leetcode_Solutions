from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nge_map = [-1] * n
        st=[]

        for i in range(2*n-1,-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if i<n:
                if st:
                    nge_map[i] = st[-1]
            
            st.append(nums[i % n])
        return nge_map

obj = Solution()
nums1 = [1, 2, 1]
nums2 = [1, 2, 3, 4, 3]
print(obj.nextGreaterElements(nums1))


