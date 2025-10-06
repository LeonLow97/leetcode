# 703 - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    # Time: O(n log k), Space: O(k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

    # Time: O(log n), Space: O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] if len(self.minHeap) else None