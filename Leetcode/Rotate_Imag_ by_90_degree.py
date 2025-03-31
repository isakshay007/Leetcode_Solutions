class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)

print("The Final matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))