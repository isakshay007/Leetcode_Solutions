from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k:int)->int:
        lsum=0
        rsum=0
        maxsum=0
        rindex = len(cardPoints)-1
        for i in range(k):
            lsum = lsum+ cardPoints[i]
            maxsum = lsum
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum+ cardPoints[rindex]
            rindex-=1
            maxsum = max(maxsum,lsum+rsum)
        return maxsum
    
cardPoints = [1,2,3,4,5,6,1]
k = 3
obj = Solution()
print(obj.maxScore(cardPoints,k))


