'''
Difficulty: MEDIUM
No.75    https://leetcode.com/problems/sort-colors/
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # base case
        if len(nums) == 1: return nums

        # define pointers
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                self.swapElem(nums, left, right)
                left += 1
                right += 1
            else:
                right += 1
        right = left

        while right < len(nums):
            if nums[right] == 1:
                self.swapElem(nums, left, right)
                left += 1
                right += 1
            else:
                right += 1

    def swapElem(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp

S = Solution()
print(S.sortColors([2, 0, 2, 1, 1, 0])); # [0,0,1,1,2,2]
print(S.sortColors([2, 0, 1])); # [0,1,2]