from typing import List

class Solution:
    def findKth(self, nums1: List[int], nums2: List[int], k : int):
        i=0
        j=0
        cnt=0
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        ele=-1
        
        while(i<n1 and j<n2):
            if nums1[i]<nums2[j]:
                if cnt == k-1:
                    ele = nums1[i]
                cnt+=1
                i+=1
            else:
                if cnt == k-1:
                    ele = nums2[j]
                cnt+=1
                j+=1
            
        while(i<n1):
            if cnt == k-1:
                ele = nums1[i]
            cnt+=1
            i+=1
        
        while(j<n2):
            if cnt == k-1:
                ele = nums2[j]
            cnt+=1
            j+=1
        
        return ele

        

nums1 = [2, 3, 6, 7, 9]
nums2= [1, 4, 8, 10]
k = 5
solution = Solution()
ans = solution.findKth(nums1,nums2,k)
print(ans)