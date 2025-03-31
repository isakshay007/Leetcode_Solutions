class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        n = len(s)
        left=0
        hash_map = [-1]*256
        for right in range(n):
            if hash_map[ord(s[right])] !=-1:
                left = max(left,hash_map[ord(s[right])]+1)
            hash_map[ord(s[right])] = right
            maxlen = max(maxlen,right-left+1)
            
        return maxlen

obj = Solution()
s= "abcabcbb"
r = obj.lengthOfLongestSubstring(s)
print(r)