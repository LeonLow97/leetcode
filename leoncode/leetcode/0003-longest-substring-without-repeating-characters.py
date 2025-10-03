# 3 - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Optimal: Sliding Window
# Time: O(n)
# Space: O(n) assuming every character is unique (worst case)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right = 0, 0
        res = 0

        while right < len(s):
            while left < right and s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            res = max(res, len(seen))
            right += 1
        
        return res
