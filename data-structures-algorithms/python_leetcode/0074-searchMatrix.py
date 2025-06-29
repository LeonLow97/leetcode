'''
Difficulty: Medium
No.74    https://leetcode.com/problems/search-a-2d-matrix/
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            # define pointers
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + (right - left) // 2

                if nums[middle] == target:
                    return True

                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

        return False

S = Solution()
print(S.searchMatrix([[1],[3]], 3)) # True