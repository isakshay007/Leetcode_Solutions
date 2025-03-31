from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)  
        window = defaultdict(int)  
        have, need_count = 0, len(need) 
        left = 0
        min_len = float('inf')
        min_window = ""

        for right in range(len(s)):
            char = s[right]
            window[char] += 1  

            if char in need and window[char] == need[char]:  
                have += 1

            while have == need_count:  
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1  
                left += 1  

        return min_window if min_len != float("inf") else ""


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(sol.minWindow("a", "a"))  # Output: "a"
print(sol.minWindow("a", "aa"))  # Output: ""
