from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols= len(matrix[0])
        height=[0]*cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    height[j] = height[j]+1
                else:
                    height[j] = 0
            for j in range(cols):
                if height[j]>0:
                    left = j
                    while left>=0 and height[left]>=height[j]:
                        left-=1
                    right = j
                    while right<cols and height[right]>=height[j]:
                        right+=1
                    width = right - left -1
                    area = width *height[j]
                    max_area = max(area,max_area)
        return max_area
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

sol = Solution()
print(sol.maximalRectangle(matrix))