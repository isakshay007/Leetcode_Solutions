class Solution:

    def numofdays(self,weights: list[int], mid: int):
        days=1
        load=0
        n = len(weights)
        for i in range(n):
            if load + weights[i]>mid:
                days+=1
                load = weights[i]
            else:
                load+=weights[i]
        return days

    def shipWithinDays(self, weights: list[int], d: int) -> int:
        low= max(weights)
        high = sum(weights)
        while(low<=high):
            mid = (low+high)//2
            numberofdays= self.numofdays(weights,mid)
            if numberofdays<=d:
                high = mid-1
            else:
                low = mid+1
        return low
            
        
solution = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
days = 1
print(solution.shipWithinDays(weights,days))
