'''
Difficulty: MEDIUM
No.33    https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # define binary pointers
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target: return middle
            if nums[left] == target: return left
            if nums[right] == target: return right

            # left sorted portion
            if nums[middle] > nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            # right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1

S = Solution()
print(S.search([4,5,6,7,0,1,2], 4)) # 0
print(S.search([4,5,6,7,0,1,2], 2)) # 6
print(S.search([4,5,6,7,0,1,2], 3)) # -1
print(S.search([6,7,0,1,2,4,5], 3)) # -1
print(S.search([6,7,0,1,2,4,10], 3)) # -1
print(S.search([1], 0)) # -1
print(S.search([1,3], 2)) # -1
print(S.search([1,3,5], 2)) # -1



