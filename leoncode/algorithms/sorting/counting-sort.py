'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# Using normal sort library and sort algorithm will take O(n log n) time complexity.
# We can solve this problem in O(n) time complexity and O(1) space complexity.
# This is the "Dutch National Flag Problem" proposed by Edsger Dijkstra.
# To use this algorithm, ensure the unique numbers we are sorting is fixed, in this case it is 3 unique numbers.

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
'''

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
