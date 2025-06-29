'''
Difficulty: MEDIUM
No.1004    https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array
if you can flip at most k 0's

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length
'''
 
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # base case
        if len(nums) == 1: return 1

        # define sliders
        left = 0
        right = 0
        counter = 0
        maxLen = -float('inf')
        
        while right < len(nums):
            if nums[right] == 0:
                counter += 1
            
            while counter > k:
                if nums[left] == 0:
                    counter -= 1
                left += 1

            maxLen = max(maxLen, right-left+1)
            right += 1

        return maxLen if maxLen != -float('inf') else 0

S = Solution()
print(S.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(S.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10