from typing import List

class Solution:
    def possible(self, bloomDay: List[int], day: int, m: int, k: int) -> bool:
        n = len(bloomDay)
        cnt = 0 
        noOfBouquets = 0  

        for i in range(n):
            if bloomDay[i] <= day:
                cnt += 1
                if cnt == k: 
                    noOfBouquets += 1
                    cnt = 0 
            else:
                cnt = 0  

        return noOfBouquets >= m  

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        val = m * k
        n = len(bloomDay)
        if val > n:  
            return -1
        low = min(bloomDay)  
        high = max(bloomDay)  
        while low <= high:
            mid = (low + high) // 2  
            if self.possible(bloomDay, mid, m, k):  # Check if feasible in `mid` days
                high = mid - 1 
            else:
                low = mid + 1  

        return low  

solution = Solution()
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(solution.minDays(bloomDay, m, k))  # Output: 3

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
print(solution.minDays(bloomDay, m, k))  # Output: -1


bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(solution.minDays(bloomDay, m, k))  # Output: 12
