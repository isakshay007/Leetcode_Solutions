class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]== nums[j-1]: 
                    continue
                k=j+1
                l=n-1

                while(k<l):
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif sum>target:
                        l-=1
                    else:
                        k+=1

        return ans

solution = Solution()
arr = [-1,0,1,2,-1,-4]
target=0
print(solution.fourSum(arr,target))


