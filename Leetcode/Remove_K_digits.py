
class Solution:
    def removeKdigits(self, num: str, k: int):
        st=[]
        n=len(num)
        for i in range(n):
            while st and k>0 and st[-1] > num[i]:
                st.pop()
                k = k-1
            st.append(num[i])
        while k>0:
            st.pop()
            k-=1
        
        res = ''.join(st).lstrip('0')

        if res:
            return res
        else:
            return "0"
obj = Solution()
print(obj.removeKdigits("1432219", 3)) 