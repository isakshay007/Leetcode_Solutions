from typing import List
class Solution:
    def isValid(self,board: List[List[str]], row:int, col:int, c:str):
        for i in range(9):
            if board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
                return False
        return True
        

    def solveSudoku(self, board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    for c in "123456789":
                        if self.isValid(board,i,j,c):
                            board[i][j]=c
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

obj = Solution()
res=obj.solveSudoku(board)
print(res)
                        
for row in board:
    print(row)
