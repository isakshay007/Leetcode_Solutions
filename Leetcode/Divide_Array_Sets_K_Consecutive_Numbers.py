from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if len(nums) % k != 0:
            return False
        
        no_count = Counter(nums) 

        sorted_no = sorted(no_count.keys()) 
        
        for i in sorted_no:  
            while no_count[i] > 0: 
                for j in range(k):
                    if i + j not in no_count or no_count[i + j] == 0:
                        return False  
                    no_count[i + j] -= 1  

        return True  
nums = [1,2,3,3,4,4,5,6]
k = 4
sol = Solution()
print(sol.isPossibleDivide(nums,k))