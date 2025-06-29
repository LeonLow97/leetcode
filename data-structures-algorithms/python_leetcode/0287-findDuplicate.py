'''
Difficulty: Medium
No.287    https://leetcode.com/problems/find-the-duplicate-number/
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            # move the pointers
            slow = nums[slow]
            fast = nums[nums[fast]]

            # found the intersection of slow and fast pointer
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow