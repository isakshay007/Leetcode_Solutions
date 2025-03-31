from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        st = []  
        nge_map = {}  

        for i in reversed(nums2):
            while st and st[-1]<=i:
                st.pop()
            
            if st:
                nge_map[i] = st[-1]
            else:
                nge_map[i] = -1

            st.append(i)
        
        result=[]
        for i in nums1:
            result.append(nge_map[i])
        return result


# Example usage
obj = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(obj.nextGreaterElement(nums1, nums2))  



