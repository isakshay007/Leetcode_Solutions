from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def solve(ind, expr, curr_val, last_operand):
            if ind == len(num):
                if curr_val == target:
                    res.append(expr)
                return
            
            for i in range(ind, len(num)):
                if i > ind and num[ind] == '0': 
                    break

                curr_str = num[ind:i+1]
                curr_num = int(curr_str)

                if ind == 0:
                    solve(i + 1, curr_str, curr_num, curr_num)
                else:
                    solve(i + 1, expr + "+" + curr_str, curr_val + curr_num, curr_num)
                    solve(i + 1, expr + "-" + curr_str, curr_val - curr_num, -curr_num)
                    solve(i + 1, expr + "*" + curr_str, curr_val - last_operand + last_operand * curr_num, last_operand * curr_num)

        solve(0, "", 0, 0)
        return res
        
obj = Solution()
print(obj.addOperators("123", 6))  
