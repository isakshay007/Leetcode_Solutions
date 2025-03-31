from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])

        def searchNext(row:int,col:int,ind:int)->bool:
            if ind == len(word):
                return True
            if row<0 or col<0 or row>=m or col>=n or board[row][col]!=word[ind]:
                return False
            temp = board[row][col]
            board[row][col] = "!"

            found = (searchNext(row-1,col,ind+1) or
                    searchNext(row,col-1,ind+1) or
                    searchNext(row+1,col,ind+1) or
                    searchNext(row,col+1,ind+1))
            
            board[row][col] = temp
            return found
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and searchNext(i,j,0):
                    return True
        return False