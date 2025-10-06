# 58 - https://leetcode.com/problems/length-of-last-word/

# Time: O(n)
# Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        start, end = 0, 0

        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                end = i
                break

        while i >= 0:
            if s[i] == " ":
                break
            else:
                start = i
                i -= 1

        return len(s[start : end + 1])
