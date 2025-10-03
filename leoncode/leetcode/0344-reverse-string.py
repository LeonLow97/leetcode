# 344 - https://leetcode.com/problems/reverse-string/

# Optimal (Two Pointers)
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
