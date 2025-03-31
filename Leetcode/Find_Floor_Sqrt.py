class Solution:
    def floorSqrt(self, n:int):
        low= 1
        high= n
        ans=1
        while(low<=high):
            mid = (low+high)//2
            if mid * mid  <= n:
                ans=mid
                low=mid+1
            else: 
                high=mid-1

        return ans
        
solution = Solution()
n=28
result = solution.floorSqrt(n)
print(result)

