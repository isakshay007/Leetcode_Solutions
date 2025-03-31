class Solution:
    def Solve(self,a:list,k:int)->list:
        n=len(a)
        count=0
        for i in range(n):
            XOR = 0
            for j in range(i,n):
                XOR += XOR ^ a[j]
                if XOR == k:
                    count+=1
        return count

                 
if __name__=="__main__":
    arr= [4, 2, 2, 6, 4]
    k=6
    solution = Solution()
    print(solution.Solve(arr,k))