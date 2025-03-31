class Solution:
    def merge(self, arr: list[list[int]]) -> list[list[int]]:
        n = len(arr)
        arr.sort()
        ans=[]
        for i in range(n):
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            else:
                ans[-1][1] = max(ans[-1][1],arr[i][1])
        return ans


solution = Solution()
intervals= [[1,3],[2,6],[8,10],[15,18]]
result=solution.merge(intervals)
print(result)
