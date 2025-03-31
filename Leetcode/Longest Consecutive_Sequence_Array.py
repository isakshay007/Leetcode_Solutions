class solution:
    
    def longestSuccessiveElements(self,a : list[int]) -> int:
        a.sort()
        n=len(a)
        cnt=0
        last_small=-1
        longest=1
        for i in range(n):
            if a[i]-1 == last_small:
                cnt+=1
                last_small=a[i]
            elif a[i]!= last_small:
                cnt=1
                last_small=a[i]
            longest = max(longest,cnt)
        return longest

solution = solution()
arr= [3, 8, 5, 7, 6]
print(solution.longestSuccessiveElements(arr))

