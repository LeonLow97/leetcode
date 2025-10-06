# 387 - https://leetcode.com/problems/first-unique-character-in-a-string/

# Time: O(n)
# Space: O(1) - since the character set is limited (e.g., ASCII

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charToCount = {}
        for char in s:
            charToCount[char] = 1 + charToCount.get(char, 0)

        for i, char in enumerate(s):
            if charToCount[char] == 1:
                return i

        return -1