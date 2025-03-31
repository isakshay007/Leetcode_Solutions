class Solution:
    def canweplace(self,stalls,mid,k):
        n=len(stalls)
        cntcows = 1
        last= stalls[0]
        for i in range(1,n):
            if stalls[i] - last >=mid:
                cntcows+=1
                last = stalls[i]
            if cntcows>=k:
                return True
        return False


    def aggressiveCows(self,stalls,k):
        n=len(stalls)
        stalls.sort()
        low = 1
        high = stalls[n-1] - stalls[0]
        while(low<=high):
            mid=(low+high)//2
            if self.canweplace(stalls,mid,k):
                low = mid+1
            else:
                high = mid-1
        return high

solution = Solution()
stalls = [0,3,4,7,10,9]
k = 6 
print(solution.aggressiveCows(stalls,k))