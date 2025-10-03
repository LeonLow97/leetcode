# 11 - https://leetcode.com/problems/container-with-most-water/

# Optimal: Two Pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            res = max(res, w*h)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return res
