from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
                     "7":"pqrs", "8":"tuv", "9":"wxyz", 
                     }
        res = []

        def helper(ind: int , path: str):
            if len(digits)== ind:
                res.append(path)
                return
            possible_letters = phone_map[digits[ind]]
            for letter in possible_letters:
                helper(ind+1,path+letter)
        helper(0,"")
        return res
