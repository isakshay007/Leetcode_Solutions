from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[]
        counter=Counter(nums)
        for num,count in counter.items():
            if count>(n//3):
                res.append(num)
        return res

solution=Solution()
arr = [11, 33, 33, 11, 33, 11]
print(solution.majorityElement(arr))
