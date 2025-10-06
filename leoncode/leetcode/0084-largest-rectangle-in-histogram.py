# 84 - https://leetcode.com/problems/largest-rectangle-in-histogram/

# Time: O(n)
# Space: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = []
        res = 0

        for i in range(len(heights)):
            height = heights[i]

            if not stack:
                stack.append((height, i))
                continue

            extended_idx = i
            while stack and height < stack[-1][0]:
                h, idx = stack.pop()
                w = i - idx
                area = h * w
                res = max(res, area)
                extended_idx = idx

            stack.append((height, extended_idx))

        for s in stack:
            h, i = s
            w = len(heights) - i
            area = h * w
            res = max(res, area)
        
        return res