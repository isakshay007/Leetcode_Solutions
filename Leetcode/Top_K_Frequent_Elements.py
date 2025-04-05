from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket=[]
        for _ in range(len(nums)+1):
            bucket.append([])

        for nums,freq in count.items():
            bucket[freq].append(nums)

        result=[]

        for i in range(len(bucket)-1,0,-1):
            if bucket[i]:
                result.extend(bucket[i])
            if len(result)>k:
                break
        return result[:k]

solution = Solution()


nums = [1, 1, 1, 2, 2, 3]
k = 2


result = solution.topKFrequent(nums, k)


print(result)
