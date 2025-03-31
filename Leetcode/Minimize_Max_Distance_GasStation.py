class Solution:
    def minimiseMaxDistance(self, arr, k):
        n=len(arr)
        howmany=[0]*(n-1)
        for i in range(1,k+1):
            maxsection=-1
            maxind=-1
            for j in range(n-1):
                diff = arr[j+1]-arr[j]
                sectionlength = diff / (howmany[j]+1)
                if sectionlength>maxsection:
                    maxsection=sectionlength
                    maxind=j
            howmany[maxind]+=1
       
        maxAns=-1
        for i in range(n-1):
            diff = arr[i+1]-arr[i]
            sectionlength = diff / (howmany[i]+1)
            maxAns = max(maxAns,sectionlength)
        return maxAns



arr = [1, 2, 3, 4, 5]
k = 4
solution = Solution()
ans = solution.minimiseMaxDistance(arr, k)
print("The answer is:", ans)
