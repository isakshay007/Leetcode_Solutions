from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n

        water_trapped = 0

        leftMax[0] = height[0]
        for i in range(n):
            leftMax[i] = max(leftMax[i-1],height[i])

        rightMax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])

        for i in range(n):
            water_trapped+= min(leftMax[i],rightMax[i])-height[i]
        return water_trapped



arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
obj = Solution()
print(f"The water that can be trapped is {obj.trap(arr)}")  # Output: 6
