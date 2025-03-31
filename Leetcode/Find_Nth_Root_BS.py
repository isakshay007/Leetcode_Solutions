class Solution:
    def fun(self,mid,n,m):
        ans=1
        for i in range(1,n+1):
            ans = ans * mid
            if ans > m:
                return 2
        if ans == m:
            return 1
        return 0
            
    def NthRoot(self, n:int, m:int)->int:
        low=1
        high=m
        while(low<=high):
            mid = (low+high)//2
            midN = self.fun(mid,n,m)
            if midN == 1:
                return mid
            elif midN == 0:
                low=mid+1
            else:
                high=mid-1
        return -1

        
solution = Solution()
n = 4
m = 69
result = solution.NthRoot(n,m)
print(result)

