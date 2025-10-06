# 392 - https://leetcode.com/problems/is-subsequence/

# Time: O(n)
# Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": 
            return True

        currentIndex = 0

        for charT in t:
            charS = s[currentIndex]
            if charT == charS:
                currentIndex += 1
                if currentIndex >= len(s):
                    break

        return True if currentIndex == len(s) else False