# 647 - https://leetcode.com/problems/palindromic-substrings/

# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    res += 1
                    dp[i][j] = True

        return res