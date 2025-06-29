'''
Difficulty: Easy
No.283    https://leetcode.com/problems/move-zeroes/
'''

from typing import List

class Solution:
    def swapElem(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp

    def moveZeroes(self, nums: List[int]) -> None:
        # base case
        if len(nums) == 1: return nums

        # define pointers
        left = 0
        right = left + 1

        # iterate through the list
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    self.swapElem(nums, left, right)
                    left += 1
            else:
                left += 1
            right += 1