from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s):
        left=0
        count = defaultdict(int)
        result=0

        for right in range(len(s)):
            count[s[right]]+=1

            while count['a']>0 and count['b']>0 and count['c']>0:
                count[s[left]]-=1
                left+=1

            result+=left
        return result

s = "abcabc"
ob = Solution()
print(ob.numberOfSubstrings(s))