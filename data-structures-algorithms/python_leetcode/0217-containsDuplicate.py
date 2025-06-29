'''
Difficulty: Easy
No.217    https://leetcode.com/problems/contains-duplicate/
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # define frequency counter
        freqCounter = {}

        for idx, num in enumerate(nums):
            if num not in freqCounter:
                freqCounter[num] = 1
            else:
                return True
            
        return False

S = Solution()
print(S.containsDuplicate([1,2,3,1]))
print(S.containsDuplicate([1,2,3,4]))
print(S.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))