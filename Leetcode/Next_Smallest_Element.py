from typing import List
class Solution:
    def NextSmallestElement(self, nums: List[int]):
        n = len(nums)
        st=[]
        sme_map=[]
        for i in range(n):
            while st and st[-1]>=nums[i]:
                st.pop()
            if st:
                sme_map.append(st[-1])
            else:
                sme_map.append(-1)
            
            st.append(nums[i])
        return sme_map


obj = Solution()
nums1 = [4, 5, 2, 10, 8]
nums2 = [3, 2, 1]

print(obj.NextSmallestElement(nums1))  # Output: [-1, 4, -1, 2, 2]
print(obj.NextSmallestElement(nums2))  # Output: [-1, -1, -1]