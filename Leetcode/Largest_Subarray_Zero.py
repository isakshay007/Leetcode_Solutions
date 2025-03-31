class Solution:
    def solve(self,a: list)->list:
        n=len(a)
        maxx=0
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=a[j]
                if sum==0:
                    maxx = max(maxx,j-i+1)
        return maxx

if __name__== "__main__":
    arr=[9, -3, 3, -1, 6, -5]
    solution = Solution()
    result = solution.solve(arr)
    print(result)
    
