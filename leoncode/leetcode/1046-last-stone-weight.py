# 1046 - https://leetcode.com/problems/last-stone-weight/

# Time: O(n log n)
# Space: O(n)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heavier = -heapq.heappop(stones)
            lighter = -heapq.heappop(stones)
            diff = heavier - lighter
            heapq.heappush(stones, -diff)
        
        return -stones[0] if len(stones) == 1 else 0
