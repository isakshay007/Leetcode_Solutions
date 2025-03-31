from typing import List
class Solution:
    def asteroidCollision(self, asteriods: List[int]):
        n=len(asteriods)
        st=[]
        
        for i in range(n):
            if asteriods[i]>0:
                st.append(asteriods[i])
            
            else:

                while st and st[-1] >0 and st[-1] < abs(asteriods[i]):
                    st.pop()
                
                if st and st[-1] == abs(asteriods[i]):
                    st.pop()
                
                elif not st or st[-1]<0:
                    st.append(asteriods[i])

        return st
obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))  # Output: [5,10]
