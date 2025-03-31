from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds=[]
        def findCombination(ind:int,target:int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                findCombination(ind,target-candidates[ind])
                ds.pop()
            findCombination(ind+1,target)
        findCombination(0,target)
        return ans

obj = Solution()
candidates = [2,3,6,7]
target = 7
ans = obj.combinationSum(candidates,target)
print(ans)
