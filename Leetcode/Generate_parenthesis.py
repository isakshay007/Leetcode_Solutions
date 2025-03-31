from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(output: str, open_count: int, close_count: int):
            
            if open_count == n and close_count == n:
                result.append(output)
                return
            
            if open_count < n:
                backtrack(output + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(output + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result

# Example usage
solution = Solution()
print(solution.generateParenthesis(3))