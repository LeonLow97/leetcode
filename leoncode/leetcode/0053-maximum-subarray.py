# 53 - https://leetcode.com/problems/maximum-subarray/

# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, current = nums[0], 0

        for i in range(len(nums)):
            current = max(nums[i], current + nums[i])
            res = max(res, current)
        
        return res