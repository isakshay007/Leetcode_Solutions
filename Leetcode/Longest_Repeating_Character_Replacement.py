class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}  
        l = 0 
        r  =0
        maxfreq = 0  
        maxlen = 0  

        for r in range(len(s)): 
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            maxfreq = max(maxfreq, freq_map[s[r]])

            while (r - l + 1) - maxfreq > k:
                freq_map[s[l]] -= 1
                l += 1 

            maxlen = max(maxlen, r - l + 1)

        return maxlen


s = "ABAB"
k = 2
obj = Solution()
print(obj.characterReplacement(s,k))