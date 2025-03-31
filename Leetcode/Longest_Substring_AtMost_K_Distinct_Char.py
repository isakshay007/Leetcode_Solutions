from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int)->int:
        if k==0:
            return 0
        max_len=0
        left=0
        right=0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]]+=1
            while len(count)>k:
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
    

sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct("eceba", 2)) 
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))    
print(sol.lengthOfLongestSubstringKDistinct("aabbcc", 2))