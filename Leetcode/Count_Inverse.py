from typing import List
class Solution:
    def number_of_inversions(self,a: List):
        n=len(a)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                if a[j]<a[i]:
                    cnt+=1
        return cnt


arr = [5,4,3,2,1]
solution = Solution()
print(solution.number_of_inversions(arr))
