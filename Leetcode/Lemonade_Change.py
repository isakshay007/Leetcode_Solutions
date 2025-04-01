from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int])->bool:
        fives=0
        tens=0
        n = len(bills)
        for i in range(n):
            if bills[i]== 5:
                fives+=1
            elif bills[i]== 10:
                if fives:
                    tens+=1
                    fives-=1
                else:
                    return False
            else:
                if fives and tens:
                    tens-=1
                    fives-=1
                elif fives:
                    fives-=3
                else:
                    return False
        return True

sol = Solution()
print(sol.lemonadeChange([5, 5, 5, 10, 20])) 
print(sol.lemonadeChange([5, 5, 10, 10, 20])) 