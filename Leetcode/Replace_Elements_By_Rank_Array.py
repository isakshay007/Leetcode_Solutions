from collections import defaultdict
class Solution:
    def rank_elements(self, arr):
        n  = len(arr)
        brr = sorted(arr)
        rank_map = defaultdict(int)

        rank=1
        for i in brr:
            if i not in rank_map:
                rank_map[i]=rank
                rank+=1

        result=[]
        for i in arr:
            result.append(rank_map[i])
        return result


arr1 = [20, 15, 26, 2, 98, 6]
sol = Solution()
output1 = sol.rank_elements(arr1)
print(output1)  