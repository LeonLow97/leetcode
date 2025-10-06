# 162 - https://leetcode.com/problems/find-peak-element/

# Time: O(log n) - binary search
# Space: O(1) - constant space

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # define pointers (binary search)
        left = 0
        right = len(nums) - 1

        # iterate through the list
        while left <= right:
            middle = left + (right - left) // 2

            # left neighbour greater (m > 0 to ensure that we are not at the start of the list)
            if middle > 0 and nums[middle] < nums[middle - 1]:
                right = middle - 1
            elif middle < len(nums) - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                return middle
            