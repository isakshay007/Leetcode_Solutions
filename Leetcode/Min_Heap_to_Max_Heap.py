class Solution:
    def maxHeapify(self,arr,n,i):
        largest=i
        left = 2*i+1
        right = 2*i+2

        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right

        if largest!=i:
            arr[i], arr[largest] = arr[largest],arr[i]
            self.maxHeapify(arr,n,largest)

    def convert_to_maxHeap(self,arr,n):
        for i in range(n//2-1,-1,-1):
            self.maxHeapify(arr,n,i)
        return arr

sol = Solution()
n = 4
arr = [1, 2, 3, 4]
print(sol.convert_to_maxHeap(arr,n))