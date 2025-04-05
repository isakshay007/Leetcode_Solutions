class Solution:
    def checkValidString(self, s:str)->bool:
        min=0
        max=0
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                min=min+1
                max=max+1
            elif s[i]==")":
                min=min-1
                max=max-1
            else:
                min=min-1
                max=max+1
            
            if min<0:
                min=0
            if max< 0:
                return False
        return min == 0
print(Solution().checkValidString("(*)"))    