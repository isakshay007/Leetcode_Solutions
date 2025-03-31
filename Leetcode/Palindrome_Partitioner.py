from typing import List
class Solution:
    def Partitioner(self, s: str)-> List[List[str]]:
        res=[]
        path=[]

        def helper(ind:int):
            if ind == len(s):
                res.append(path[:])
                return
            for i in range(ind,len(s)):
                if isPalindrome(s,ind,i):
                    path.append(s[ind:i+1])
                    helper(i+1)
                    path.pop()

        def isPalindrome(s:str,start:int,end:int):
            while start<end:
                if s[start]!= s[end]:
                    return False
                start+=1
                end-=1
            return True
        helper(0)
        return res
s="aabb"
obj = Solution()
ans = obj.Partitioner(s)
print(ans)
