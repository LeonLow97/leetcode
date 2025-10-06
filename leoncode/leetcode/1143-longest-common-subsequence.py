# 1143 - https://leetcode.com/problems/longest-common-subsequence/

# Time: O(m*n) where m and n are the lengths of text1 and text2
# Space: O(m*n) for the dp array

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # set up dp '0's on grid and also include out of bounds position
        dp = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
