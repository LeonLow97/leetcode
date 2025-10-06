# 151 - https://leetcode.com/problems/reverse-words-in-a-string/

# Time: O(n)
# Space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        parts = []

        temp = ""
        for char in s:
            if char != " ":
                first = False
                temp += char
            else:
                if temp:
                    parts.append(temp)
                temp = ""

        if temp:
            parts.append(temp)

        res = []
        for i in range(len(parts) - 1, -1, -1):
            res.append(parts[i])

        return " ".join(res)