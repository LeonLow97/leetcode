# 1004 - https://leetcode.com/problems/max-consecutive-ones-iii/

# Time: O(n) - we traverse the list once with two pointers
# Space: O(1) - we use constant space

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