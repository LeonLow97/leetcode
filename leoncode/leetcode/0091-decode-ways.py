# 91 - https://leetcode.com/problems/decode-ways/

# Time: O(n)
# Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        # DP (top-down), include the first char or the first 2 chars
        # then the rest will be the subproblem
        def dfs(i):
            # base case
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in dp:
                return dp[i]

            res = 0
            res += dfs(i+1) # subproblem 1, include first char

            # subproblem 2, include first 2 chars
            if i+1 < len(s) and (s[i] == "1" or
                (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)

            dp[i] = res
            return dp[i]

        return dfs(0)