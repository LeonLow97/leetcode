'''
Difficulty: EASY
No.704    https://leetcode.com/problems/binary-search/
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define pointers
        left = 0
        right = len(nums) - 1

        # iterate through the list
        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1

        return -1