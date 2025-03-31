from typing import List

class Solution:
    def maxelem(self, mat: List[List[int]], col: int)->int:
        max_row=0
        for i in range(len(mat)):
            if mat[i][col] > mat[max_row][col]:
                max_row=i
        return max_row
        

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        col= len(mat[0])
        low=0
        high=col-1
        while(low<=high):
            mid=(low+high)//2
            row= self.maxelem(mat,mid)
            left = mat[row][mid-1] if mid-1>=0 else -1
            right =  mat[row][mid+1] if mid+1<col else-1
            if mat[row][mid] > right and mat[row][mid] > left:
                return [row,mid]
            elif mat[row][mid] <left:
                high=mid-1
            else:
                low=mid+1


mat = [[1, 4, 7, 11], [3, 5, 8, 12], [6, 10, 9, 16], [14, 13, 11, 17]]
solution = Solution()
result = solution.findPeakGrid(mat)
print(result)  