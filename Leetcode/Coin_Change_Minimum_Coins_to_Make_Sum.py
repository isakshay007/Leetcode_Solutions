class Solution:
    def Min_Coins(self, coins, V):
        coins.sort(reverse = True)
        ans=[]

        for coin in coins:
            while V  >= coin:
                V-= coin
                ans.append(coin)
        return ans
V = 49
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
obj = Solution()
ans = obj.Min_Coins(coins, V)

print("The minimum number of coins is", len(ans))
print("The coins are")
for coin in ans:
    print(coin, end=" ")