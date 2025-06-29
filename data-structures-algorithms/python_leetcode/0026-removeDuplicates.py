'''
Difficulty: EASY
No.26    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # base case 
        if len(nums) == 1: return nums[0]

        # define pointers
        left = 0
        right = left + 1

        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                self.swapElem(nums, left, right)
                right += 1
        
        return left + 1

    def swapElem(self, nums: List[int], idx1, idx2):
        temp = nums[idx2]
        nums[idx2] = nums[idx1]
        nums[idx1] = temp

S = Solution()
print(S.removeDuplicates([1,1,2])) # 2
print(S.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5

