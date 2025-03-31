class Solution:
    def findMin(self, a: list[int]) -> int:
        n=len(a)
        low=0
        high= n-1
        ans= float("inf")
        while(low<=high):
            mid = (low+high)//2

            if a[low]<=a[high]:
                ans = min(ans,a[low])
                break

            if a[low]<=a[mid]:
               ans = min(ans,a[low])
               low=mid+1
            else:
               ans = min(ans,a[mid])
               high=mid-1

        return ans
              



        
solution = Solution()
nums = [4,5,6,7,0,1,2]
result = solution.findMin(nums)
print(result)

