# 973 - https://leetcode.com/problems/k-closest-points-to-origin/

# Time: O(n) + O(k log n)
# Space: O(n)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(math.sqrt(x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(points)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(points)
            res.append([x, y])

        return res
