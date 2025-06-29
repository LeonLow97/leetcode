'''
Difficulty: MEDIUM
No.167    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # define pointers
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            
        return [left + 1, right + 1]