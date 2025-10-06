# 154 - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Time: O(log n) on average, O(n) in the worst case
# Space: O(1)

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
      # base case
      if len(nums) == 1: return nums[0]

      # define binary pointers
      left = 0
      right = len(nums) - 1

      # CASE: list is already sorted
      if nums[0] < nums[right]: return nums[0]

      # iterate through the list
      while left < right:
         middle = left + (right - left) // 2

         if nums[middle] > nums[right]:
            left = middle + 1
         elif nums[middle] < nums[right]:
            right = middle
         elif nums[middle] == nums[right] and nums[middle] == nums[left]:
            right -= 1
            left += 1
         elif nums[middle] == nums[right]:
            right -= 1
         else:
            left += 1

      return nums[left]