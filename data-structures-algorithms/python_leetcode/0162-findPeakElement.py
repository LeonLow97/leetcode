'''
Difficulty: MEDIUM
No.162    https://leetcode.com/problems/find-peak-element/
'''

from typing import List

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
            
S = Solution()
print(S.findPeakElement([1,2,3,1])) # 2
print(S.findPeakElement([1,2,3,1,4])) # 4
print(S.findPeakElement([1,2,1,3,5,6,4])) # 5
print(S.findPeakElement([6,5,4,3,2,3,2])) # 0
print(S.findPeakElement([1,2,3,7,6,3,1])) # 3
print(S.findPeakElement([0,2,3,1,5,4,5])) # 6



