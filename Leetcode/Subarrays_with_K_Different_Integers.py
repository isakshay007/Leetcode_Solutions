from collections import defaultdict
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k:int):
        return self.countKDistinct(nums,k) - self.countKDistinct(nums,k-1)
    def countKDistinct(self,nums: List[int], k:int):
        if k==0:
            return 0
        left=0
        count = defaultdict(int)
        result=0
        for right in range(len(nums)):
            count[nums[right]]+=1
            if count[nums[right]]==1:
                k-=1
            while k<0:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    k+=1
                left+=1
            result+=right-left+1
        return result

sol = Solution()
print(sol.subarraysWithKDistinct([1,2,1,2,3], 2)) 


        
