class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                sum = nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1

        return ans

solution = Solution()
arr = [-1,0,1,2,-1,-4]
print(solution.threeSum(arr))


