'''
Difficulty: MEDIUM
No.209    https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # define window
        left = 0
        right = 0

        # define length and sum
        total = 0
        minLen = float('inf')

        while right < len(nums):
            total += nums[right]

            while total >= target:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1
            
            right += 1
        
        if minLen == float('inf'): return 0
        return minLen

S = Solution()
print(S.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(S.minSubArrayLen(4, [1,4,4])) # 1
print(S.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0
print()
