from typing import List
class Solution:
    def  numSubarraysWithSum(self, nums: List[int], goal:int)->int:
        l1=0
        l2=0
        sum1=0
        sum2=0
        cnt=0
        for r in range(len(nums)):
            sum1+=nums[r]
            sum2+=nums[r]

            while l1<=r and sum1>goal:
                sum1-=nums[l1]
                l1+=1
            while l2<=r and sum2>=goal:
                sum2-=nums[l2]
                l2+=1
            cnt+=(l2-l1)

        return cnt



nums1 = [1, 0, 1, 0, 1]
goal1 = 2
sol = Solution()
print(sol.numSubarraysWithSum(nums1,goal1))
