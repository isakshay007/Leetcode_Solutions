class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        col=[0]*m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        
        for i in range(n):
            for j in range(m):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0




solution = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix)

print("The Final matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))