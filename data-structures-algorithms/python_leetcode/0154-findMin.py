'''
Difficulty: HARD
No.154    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return nums[0]

        # define binary pointers
        left = 0
        right = len(nums) - 1

        # CASE: list already sorted
        if nums[left] < nums[right]: return nums[0]

        # iterate through the list
        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
            elif nums[middle] == nums[left] and nums[middle] == nums[right]:
                right -= 1
                left += 1
            elif nums[middle] == nums[right]:
                right -= 1
            else:
                left += 1

        return nums[left]

S = Solution()
print(S.findMin([1,3,5])) # 1
print(S.findMin([2,2,2,0,1])) # 0
print(S.findMin([4,5,6,7,0,1,4])) # 0
print(S.findMin([0,1,4,4,5,6,7])) # 0
print(S.findMin([3,3,1,3])) # 1
print(S.findMin([1,1])) # 1
print(S.findMin([10,1,10,10,10])) # 1
print(S.findMin([10,10,10,1,10])) # 1

# Tutor's Solution (treating this problem as a 2-pointer)
# if mid is bigger then right, increment left pointer
# if mid is smaller than right, decrement right pointer
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # define pointers
        left = 0
        right = len(nums) - 1
        
        while (left < right):
            middle = left + (right - left) // 2

            if (nums[middle] > nums[right]):
                left += 1
            else:
                right -= 1

        return min(nums[left], nums[right])

