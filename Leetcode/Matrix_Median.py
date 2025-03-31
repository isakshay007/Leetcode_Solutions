class Solution:
    
    def upperbound(self,row,target):
        low=0
        high = len(row)-1
        while(low<=high):
            mid=(low+high)//2
            if row[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        return low
    
    def small(self,arr,mid):
        count=0
        for i in  arr:
            count=count+ self.upperbound(i,mid)
        return count

    def matrixmedian(self,arr):
        row=len(arr)
        col= len(arr[0])
        low=0
        high=10**9
        while(low<=high):
            req=(row*col)//2 
            mid = (low+high)//2
            smallequals = self.small(arr,mid)
            if smallequals<=req:
                low=mid+1
            else:
                high = mid-1
        return low
matrix = [
    [1, 2, 3, 4, 5],
    [8, 9, 11, 12, 13],
    [21, 23, 25, 27, 29]
]
solution = Solution()
ans = solution.matrixmedian(matrix)
print(ans)