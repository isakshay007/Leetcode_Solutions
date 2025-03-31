from typing import List
class Solution:
    def Subset_Sum(self, arr: List[int], n: int)-> List[int]: 
        ans=[]

        def sumhelper(ind:int, sum:int):
            if ind==n:
                ans.append(sum)
                return
            sumhelper(ind+1,sum+arr[ind])
            sumhelper(ind+1,sum)
        sumhelper(0,0)
        ans.sort()
        return ans
obj = Solution()
arr=[3,1,2]
res = obj.Subset_Sum(arr,len(arr))
print(res)
        
