'''
Difficulty: MEDIUM
No.80    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

from typing import List

class Solution:
    def swapElem(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp

    def removeDuplicates(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return 1
        if len(nums) == 2: return 2

        # define pointers
        left = 0
        right = left + 1
        counter = 0 # increase counter if the left and right elements are equal in value

        # iterate through the list
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                counter = 0
            elif nums[left] == nums[right] and counter == 0:
                left += 1
                counter += 1
                nums[left] = nums[right]
            right += 1
            
        return left + 1
 
S = Solution()
print(S.removeDuplicates([1,1,1,2,2,3])) # 5
print(S.removeDuplicates([0,0,1,1,1,1,2,3,3])) # 7