# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.min_heap) and  num > self.min_heap[0]:
                heappush(self.max_heap, -heappop(self.min_heap))
                heappush(self.min_heap, num)
            else:   
                heappush(self.max_heap, -num)
        else:
            heappush(self.max_heap, -num)
            heappush(self.min_heap, -heappop(self.max_heap)) 

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()