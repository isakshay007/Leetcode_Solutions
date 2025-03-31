class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        m=len(matrix[0])
        result=[]
        left=0
        right = m-1
        top=0
        bottom = n-1
        while(left<=right and top<=bottom):

            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            
            if (top<=bottom):
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1
            if (left<=right):
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left=left+1   
        return result

solution = Solution()
matrix =[[1,2,3],[4,5,6],[7,8,9]]
result=solution.spiralOrder(matrix)
print(result)
