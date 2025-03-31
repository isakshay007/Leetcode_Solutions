from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int)->int:
        sum1=0
        sum2=0
        l1=0
        l2=0
        cnt=0
        for r in range(len(nums)):
            sum1+=nums[r]%2
            sum2+=nums[r]%2

            while l1<=r and sum1>k:
                sum1-= nums[l1]%2
                l1+=1
            while l2<=r and sum2>=k:
                sum2-= nums[l2]%2
                l2+=1
            cnt +=(l2-l1)

        return cnt
    
nums = [1,1,2,1,1]
k = 3
sol = Solution()
print(sol.numberOfSubarrays(nums,k))

