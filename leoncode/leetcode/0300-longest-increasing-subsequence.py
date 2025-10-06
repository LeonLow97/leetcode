# 300 - https://leetcode.com/problems/longest-increasing-subsequence/

# Time: O(N^2)
# Space: O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # base case for elem is '1' subsequence
        dp = [1] * len(nums)

        ## DP "bottom-up" approach
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)