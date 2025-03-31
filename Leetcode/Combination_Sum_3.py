from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(start:int ,ds: List[int], remaining: int):
            if len(ds)==k and remaining==0:
                res.append(ds[:])
                return
            if len(ds)>k or remaining<0:
                return
            for i in range(start,10):
                ds.append(i)
                helper(i+1,ds,remaining-i)
                ds.pop()
        helper(1,[],n)
        return res
        