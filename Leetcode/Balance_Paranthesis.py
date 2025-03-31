class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(0,len(s)):
            if s[i]=='('or  s[i]=='['or  s[i]=='{':
                st.append(s[i])

            else:

                if len(st) == 0:
                    return False
                
                ch = st[-1]
                st.pop()
                if s[i]==')' and ch=='(' or s[i]==']' and ch=='[' or s[i]=='}' and ch=='{':
                    continue
                else:
                    return False
        return len(st)== 0
    
solution = Solution()
s= "(){}()"
print(solution.isValid(s))

        