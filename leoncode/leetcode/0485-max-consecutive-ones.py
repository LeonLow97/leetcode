# 485 - https://leetcode.com/problems/max-consecutive-ones/

# Time: O(n)
# Space: O(1)

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