'''
Difficulty: MEDIUM
No.485    https://leetcode.com/problems/max-consecutive-ones/
'''

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return 1 if nums[0] == 1 else 0

        # define sliders
        left = 0
        right = 0
        maxLen = -float('inf')

        while right < len(nums):
            if nums[right] == 1:
                maxLen = max(maxLen, right-left+1)
            else:
                left = right + 1
            right += 1

        return maxLen if maxLen != -float('inf') else 0

S = Solution()
print(S.findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3 (6 iterations)
print(S.findMaxConsecutiveOnes([1,0,1,1,0,1])) # 2 (6 iterations)
print(S.findMaxConsecutiveOnes([1])) # 1 
