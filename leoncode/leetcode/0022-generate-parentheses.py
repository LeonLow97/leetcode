# 22 - https://leetcode.com/problems/generate-parentheses/

# Time: O(4^n / sqrt(n)) - Catalan number
# Space: O(4^n / sqrt(n)) - Catalan number
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(openN, closedN):
            if closedN > openN:
                return
            if openN > n or closedN > n:
                return
            if openN == closedN == n:
                temp = stack.copy()
                res.append(''.join(temp))
                return

            # include open bracket
            stack.append("(")
            backtracking(openN + 1, closedN)
            stack.pop()

            # include closed bracket
            stack.append(")")
            backtracking(openN, closedN + 1)
            stack.pop()

        backtracking(0, 0)
        return res
