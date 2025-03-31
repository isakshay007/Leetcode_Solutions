import heapq
import sys
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert_key(self,x):
        return heapq.heappush(self.heap,x)
    
    def delete_key(self,index):
        if 0 <= index < len(self.heap):
            self.heap[index] = -sys.maxsize
            heapq.heapify(self.heap)
            heapq.heappop(self.heap)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else -1
    
def process(Q, queries):
    heap = MinHeap()
    result=[]
    for query in queries:
        q = query.split()
        if q[0]=="1":
            heap.insert_key(int(q[1]))
        elif q[0]=="2":
            heap.delete_key(int(q[1]))
        else:
            result.append(heap.extract_min())
    return result

# Example Usage
Q = 7
queries = [
    "1 4",
    "1 2",
    "3",
    "1 6",
    "2 0",
    "3",
    "3"
]

print(process(Q, queries))  # Output: [2, 6, -1]