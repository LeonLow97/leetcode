'''
Difficulty: HARD
No.42    https://leetcode.com/problems/trapping-rain-water/
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        if len(height) < 3: return 0

        # Determine the highest elevated bar
        highestIdx = 0
        for idx in range(len(height)):
            if height[idx] > height[highestIdx]:
                highestIdx = idx

        # define pointers and counter
        counter = 0
        left = 0
        right = len(height) - 1
        highestLeft = 0
        highestRight = 0
        
        while left < highestIdx:
            highestLeft = max(height[left], highestLeft)
            counter += highestLeft - height[left]
            left += 1

        while right > highestIdx:
            highestRight = max(height[right], highestRight)
            counter += highestRight - height[right]
            right -= 1

        return counter

S = Solution()
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(S.trap([4,2,0,3,2,5])) # 9