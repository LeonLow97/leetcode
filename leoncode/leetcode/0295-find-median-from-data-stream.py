# 295 - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        # left heap contains all smaller numbers, max heap
        # right heap contains all larger numbers, min heap
        self.leftHeap, self.rightHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        # check if left heap has all smaller numbers than right heap
        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))

        # ensure size of left heap not more than 1 element of size of right heap
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        
        # ensure size of right heap not more than 1 element of size of left heap
        if len(self.rightHeap) - len(self.leftHeap) > 1:
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        elif len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        else:
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2