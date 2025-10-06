# 20 - https://leetcode.com/problems/valid-parentheses/

# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {
            "}": "{", "]": "[", ")": "("
        }
        stack = [] # contains all open brackets

        for b in s:
            if b not in closedToOpen:
                stack.append(b)
            else:
                if not stack:
                    return False
                if closedToOpen[b] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
