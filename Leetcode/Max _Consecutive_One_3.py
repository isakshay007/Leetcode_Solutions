from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n=len(nums)
#        for i in range(n):
#            zeros=0
#            for j in range(n):
#                if nums[j]==0:
#                    zeros+=1
#                if zeros<=k:
#                    len = j-i+1
#                    maxlen = max(maxlen,len)
#        return maxlen

        l = 0  
        zeros = 0  
        maxlen = 0  

        for r in range(n):  
            if nums[r] == 0:
                zeros += 1  

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1 
                l += 1  

            maxlen = max(maxlen, r - l + 1)

        return maxlen

obj = Solution()
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
