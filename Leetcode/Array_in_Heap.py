class Solution:
    def heap(self,arr):
        n=len(arr)
        for i in range(n//2):
            left = 2*i+1
            right = 2*i+2

            if left<n and arr[i]<arr[left]:
                return 0

            if right<n and arr[i]<arr[right]:
                return 0
        return 1
    
sol = Solution()
arr = [9, 15, 10, 7, 12, 11]
print(sol.heap(arr))
