# 209 - https://leetcode.com/problems/minimum-size-subarray-sum/

# Time: O(n) - we go through the array once with the right pointer, and the left pointer only moves forward
# Space: O(1) - we use a constant amount of space

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