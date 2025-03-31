from typing import List
import heapq

class Solution:
    def merge_k_sorted_arrays(self,arr,k):
        min_heap=[]
        result=[]

        for i in range(k):
            if arr[i]:
                heapq.heappush(min_heap,(arr[i][0],i,0))

        while min_heap:
            value, arr_index, element_index = heapq.heappop(min_heap)
            result.append(value)

            next_index = element_index + 1

            if next_index<len(arr[arr_index]):
                heapq.heappush(min_heap,(arr[arr_index][next_index],arr_index,next_index))
                
        return result
    
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = len(arr)
s = Solution()
merged_array = s.merge_k_sorted_arrays(arr, k)
print(merged_array)