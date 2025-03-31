class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n):
            if (i==0 or nums[i-1]<nums[i])and(i==n-1 or nums[i]>nums[i+1]):
                return i
        return -1
solution = Solution()
arr = [1,2,1,3,5,6,4]
print(solution.findPeakElement(arr))
