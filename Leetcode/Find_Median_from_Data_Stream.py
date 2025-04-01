import heapq

class MedianFinder:

    def __init__(self):
        self.left=[] # max-heap
        self.right=[] #min-heap

    def addNum(self, num: int):
        if len(self.left)==0 or num<= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)


        if len(self.left)>len(self.right)+1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        elif len(self.right)>len(self.left):

            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0])/2
    

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())  # Output: 1.5
obj.addNum(3)
print(obj.findMedian())  # Output: 2.0