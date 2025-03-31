class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
    
        def pow(base,exp,mod):
            result = 1
            while exp>0:
                if exp%2==1:
                    result = (result * base) % mod
                base = (base * base)  % mod
                exp //=2
            return result

        even_no = (n+1)//2
        odd_no = n//2

        return (pow(5,even_no,MOD)* pow(4,odd_no,MOD)) % MOD

solution = Solution()
print(solution.countGoodNumbers(7))  



