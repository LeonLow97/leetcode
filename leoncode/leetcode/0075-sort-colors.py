# 75 - https://leetcode.com/problems/sort-colors/

# Optimal
# Time: O(n)
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3 # red, white, blue, this is number is fixed at 3
        for color in nums:
            counts[color] += 1

        Red, White, Blue = counts
        for i in range(Red):
            nums[i] = 0
        for i in range(Red, Red + White):
            nums[i] = 1
        for i in range(Red + White, len(nums)):
            nums[i] = 2
