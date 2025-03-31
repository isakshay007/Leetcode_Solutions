from typing import List
class Solution:
    def findhelper(self,i:int,j:int,a: List[List[int]],n: int,ans:List[str],move:str,vis:List[List[int]]):
        if i == n-1 and j == n-1:
            ans.append(move)
            return
        
        if i+1<n and not vis[i+1][j] and a[i+1][j] == 1:
            vis[i][j]=1
            self.findhelper(i+1,j,a,n,ans,move+'D',vis)
            vis[i][j]=0
        
        if j-1>=0 and not vis[i][j-1] and a[i][j-1]==1:
            vis[i][j]=1
            self.findhelper(i,j-1,a,n,ans,move+'L',vis)
            vis[i][j]=0

        if j+1<n and not vis[i][j+1] and a[i][j+1]==1:
            vis[i][j]=1
            self.findhelper(i,j+1,a,n,ans,move+'R',vis)
            vis[i][j]=0

        if i-1>=0 and not vis[i-1][j] and a[i-1][j]==1:
            vis[i][j]=1
            self.findhelper(i-1, j, a, n, ans, move+'U', vis)
            vis[i][j]=0        


    def findPath(self,m: List[List[int]],n:int)->List[str]:
        ans=[]
        vis=[[0 for _ in range(n)] for _ in range(n)]
        if m[0][0]== 1:
            self.findhelper(0,0,m,n,ans,"",vis)
        return ans


obj = Solution()
m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n=4
result = obj.findPath(m, n)
print(result)
