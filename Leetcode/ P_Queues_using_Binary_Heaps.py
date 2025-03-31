import heapq
class Maxheap:
    def __init__(self,arr):
        self.heap = [-x for x in arr] if arr else []
        heapq.heapify(self.heap)
    
    def insert(self,value):
        heapq.heappush(self.heap,-value)

    def extract_max(self):
        return -heapq.heappop(self.heap) if self.heap else None

    def get_heap(self):
        return sorted([-x for x in self.heap ], reverse = True)

arr = [4, 2, 8, 16, 24, 2, 6, 5]
max_heap = Maxheap(arr)

print("Max Heap:", max_heap.get_heap()) 
print("Extracted Max:", max_heap.extract_max())  
print("Heap after extraction:", max_heap.get_heap())