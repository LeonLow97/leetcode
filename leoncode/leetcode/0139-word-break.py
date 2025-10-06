# 139 - https://leetcode.com/problems/word-break/

# Time: O(n * m * k)
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up approach, e.g., from dp[8] to dp[0]
        dp = [False] * (len(s) + 1)   # "+1" because we include our base case

        ## base case, if we ever get to this index of the string, we found the
        ## word in our wordDict, so we return True
        dp[len(s)] = True 

        ## looping backwards, aka "bottom-up" approach
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (
                    len(s) - i >= len(w) and
                    i + len(w) <= len(s) and
                    s[i : len(w) + i] == w
                ):
                    ## we found a word! Let's cache it
                    dp[i] = dp[i + len(w)]

                # if we ever find a word that matches the index, we can go to
                # the next loop
                if dp[i]:
                    break

        return dp[0]