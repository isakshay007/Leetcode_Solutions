from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s:List[int])->int:
        g.sort()
        s.sort()
        i=0 #child pointer
        j=0 # parent pointer

        while i < len(g) and j < len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i



sol = Solution()
print(sol.findContentChildren([1, 2, 3], [1, 1])) 
print(sol.findContentChildren([1, 2], [1, 2, 3]))  
print(sol.findContentChildren([2, 3, 5], [1, 2, 3, 4])) 