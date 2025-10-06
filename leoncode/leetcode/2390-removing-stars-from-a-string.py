# 2390 - https://leetcode.com/problems/removing-stars-from-a-string/

# Time: O(n)
# Space: O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
            elif char == "*":
                if stack:
                    stack.pop()

        return ''.join(stack)
