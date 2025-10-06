# 5 - https://leetcode.com/problems/longest-palindromic-substring/

# Time: O(n^2)
# Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        # odd length palindrome
        for i in range(len(s)):
            left, right = i, i
            # perform two pointers
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curLen = right - left + 1
                if curLen > len(res):
                    res = s[left : right + 1]
                left -= 1
                right += 1

        # even length palindrome
        for i in range(len(s)):
            left, right = i, i+1
            # perform two pointers
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curLen = right - left + 1
                if curLen > len(res):
                    res = s[left : right + 1]
                left -= 1
                right += 1

        return res
