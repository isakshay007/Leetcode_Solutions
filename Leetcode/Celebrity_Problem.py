from typing import List
class Solution:
    def find_celebrity(self, mat):
        n = len(mat)
        top = 0
        down = n-1
        while top<down:
            if mat[top][down]==1:
                top+=1
            else:
                down-=1

        candidate = top
        for i in range(n):
            if i!= candidate:
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
        
        return candidate
sol = Solution()

mat1 = [[1, 1, 0], 
        [0, 1, 0], 
        [0, 1, 1]]
print(sol.find_celebrity(mat1)) 