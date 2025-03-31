class Solution:
    def fruits_in_basket(self,arr):
        maxlen=0
        n=len(arr)
        for i in range(n):
            uniq_ele = set()
            for j in range(i,n):
                uniq_ele.add(arr[j])
                if len(uniq_ele)>2:
                    break
                maxlen = max(maxlen,j-i+1)
        return maxlen

arr1 = [2, 1, 2]

obj = Solution()
print(obj.fruits_in_basket(arr1))  