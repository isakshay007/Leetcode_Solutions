class Solution:
    def search(self, a: list[int], target: int)->int:
        n=len(a)
        low=0
        high= n-1
        while(low<=high):
            mid = (low+high)//2
            if a[mid] == target:
                return mid
            
           
           #if left sorted
            if a[mid]>=a[low]:
                if a[low]<=target and target<=a[mid]:
                   high = mid-1
                else:
                   low = mid+1
            
            #if right sorted
            if a[mid]<=a[high]:
                if a[mid]<=target and target<=a[high]:
                   low = mid+1
                else:
                   high = mid-1

        return -1

        
solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
result = solution.search(nums,target)
print(result)

