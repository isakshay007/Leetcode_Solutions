import math

class Solution:
    def findmax(self, piles):
        n = len(piles)
        maxi = float('-inf')
        for i in range(n):
            maxi = max(maxi, piles[i])
        return maxi

    def func(self, arr, hourly):
       
        totalreq = 0
        for i in range(len(arr)):
            totalreq += math.ceil(arr[i] / hourly)
        return totalreq

    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        low = 1
        high = self.findmax(piles)
        ans = high 
        while low <= high:
            mid = (low + high) // 2
            totalH = self.func(piles, mid)
            if totalH <= h:
              
                ans = mid
                high = mid - 1
            else:

                low = mid + 1
        return ans


solution = Solution()
piles = [3, 6, 7, 11]
h = 8
print(solution.minEatingSpeed(piles, h))  
