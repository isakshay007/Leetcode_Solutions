from typing import List
class Solution:
    def isSafe(self,row,col,board,n):
        duprow,dupcol = row,col

        while row>=0 and col>=0:
            if board[row][col]== 'Q':
                return False
            row-=1
            col-=1

        row,col = duprow,dupcol 
        while  col>=0:
            if board[row][col]== 'Q':
                return False
            col-=1

        row,col = duprow,dupcol
        while row<n and col>=0:
            if board[row][col]== 'Q':
                return False
            row+=1
            col-=1
        return True


    def Solve(self,col,board,ans,n):
        
        if col == n:
            ans.append(list(board))
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row] = board[row][:col]+"Q"+board[row][col+1:]
                self.Solve(col+1,board,ans,n)
                board[row] = board[row][:col]+"."+board[row][col+1:]
        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board = ['.' * n for _ in range(n)]
        self.Solve(0, board, ans, n)
        return ans


Obj= Solution()
n=4
ans = Obj.solveNQueens(n)
print(ans)