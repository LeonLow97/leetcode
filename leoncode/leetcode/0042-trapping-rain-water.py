# 42 - https://leetcode.com/problems/trapping-rain-water/

# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force solution
        res = 0
        n = len(height)

        for i in range(n):
            leftMax, rightMax = height[i], height[i]

            for j in range(0, i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])
            
            res += min(leftMax, rightMax) - height[i]
        
        return res


# Optimal
# Time: O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        # Find index with highest height
        highestHeightIdx, highestHeight = 0, height[0]
        for i, h in enumerate(height):
            if h > highestHeight:
                highestHeightIdx, highestHeight = i, h

        # Increment res with water on left of highest height
        leftHighest = height[0]
        for i in range(0, highestHeightIdx):
            h = height[i]
            if h >= leftHighest:
                leftHighest = h
            else:
                res += leftHighest - h
        
        # Increment res with water on right of highest height
        rightHighest = height[-1]
        for i in range(len(height) -1, highestHeightIdx, -1):
            h = height[i]
            if h >= rightHighest:
                rightHighest = h
            else:
                res += rightHighest - h

        return res
