'''
Difficulty: EASY
No.20    https://leetcode.com/problems/valid-parentheses/
'''

# Time Complexity: O(N), Space Complexity: O(N) because we use a stack to keep track of the characters
class Solution:
    def isValid(self, s: str) -> bool:
        # base case
        if len(s) == 1: return False

        # Character array of the string
        charArr = list(s)

        stack = []

        for char in charArr:
            if char == '(' or char == "[" or char == "{":
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                if stack[-1] == "(" and char != ")": return False
                if stack[-1] == "[" and char != "]": return False
                if stack[-1] == "{" and char != "}": return False
                stack.pop()

        return len(stack) == 0
    
S = Solution()
print(S.isValid("()")) # True
print(S.isValid("()[]{}")) # True
print(S.isValid("{()}")) # True
print(S.isValid("(){}[")) # False
print(S.isValid("(]")) # False

# My Solution but lengthy
class Solution:
    def isValid(self, s: str) -> bool:
        # base case
        if len(s) == 1: return False

        # define stack
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue
            
            if stack[-1] == "(" and (char == "}" or char == "]"):
                return False
            if stack[-1] == "[" and (char == ")" or char == "}"):
                return False
            if stack[-1] == "{" and (char == "]" or char == ")"):
                return False

            if stack[-1] == "(" and char == ")":
                stack = stack[:-1]
            elif stack[-1] == "[" and char == "]":
                stack = stack[:-1]
            elif stack[-1] == "{" and char == "}":
                stack = stack[:-1]
            else:
                stack.append(char)

        if len(stack) != 0:
            return False
        return True