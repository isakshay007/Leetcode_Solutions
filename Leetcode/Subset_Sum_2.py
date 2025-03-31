from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: 
        ans=[]
        res=set()


        def sumhelper(ind:int, ds: List[int]):
            if ind==len(nums):
                ds.sort()
                res.append(tuple(ds))
                return
            ds.append(nums[ind])
            sumhelper(ind+1,ds)
            ds.pop()
            sumhelper(ind+1,ds)
        sumhelper(0,[])
        for it in res:
            ans.append(list(it))
        return ans

        
