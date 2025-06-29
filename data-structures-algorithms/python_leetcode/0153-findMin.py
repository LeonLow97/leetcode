'''
Difficulty: MEDIUM
No.153    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return nums[0]

        # define binary pointers
        left = 0
        right = len(nums) - 1

        # CASE: list already sorted so smallest element is definitely at index 0
        if nums[left] < nums[right]: return nums[0]

        # Iterate through the list
        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]
S = Solution()
print(S.findMin([3,4,5,1,2])) # 1
print(S.findMin([4,5,6,7,0,1,2])) # 0
print(S.findMin([11,13,15,17])) # 11