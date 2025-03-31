from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        cnt=0
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        ind2 = n//2
        ind1 = ind2-1
        ele1 = -1
        ele2 = -1
        
        while(i<n1 and j<n2):
            if nums1[i]<nums2[j]:
                if cnt == ind1:
                    ele1 = nums1[i]
                if cnt == ind2:
                    ele2 = nums1[i]
                cnt+=1
                i+=1
            else:
                if cnt == ind1:
                    ele1 = nums2[j]
                if cnt == ind2:
                    ele2 = nums2[j]
                cnt+=1
                j+=1
            
        while(i<n1):
            if cnt == ind1:
                ele1 = nums1[i]
            if cnt == ind2:
                ele2 = nums1[i]
            cnt+=1
            i+=1
        
        while(j<n2):
            if cnt == ind1:
                ele1 = nums2[j]
            if cnt == ind2:
                ele2 = nums2[j]
            cnt+=1
            j+=1
        
        if n%2==1:
            return float(ele2)
        else:
            return float(ele1+ele2)//2

nums1 = [1,3]
nums2 = [2]
solution = Solution()
ans = solution.findMedianSortedArrays(nums1,nums2)
print(ans)