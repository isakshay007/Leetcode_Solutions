from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:  
            return True
        
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        
        return False  

        