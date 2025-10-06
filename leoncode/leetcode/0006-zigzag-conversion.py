# 6 - https://leetcode.com/problems/zigzag-conversion/

# Time: O(n) where n is the length of the input string.
# Space: O(1)
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # base case
        if numRows == 1: return s

        # Arithmetic Progression
        result = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                result += s[i]
                # check if we are in the middle rows (get the extra characters)
                # decreases by 2 each time for the 3rd IF condition
                mid = i + increment - 2 * r
                if (r > 0 and r < numRows - 1 and mid< len(s)):
                    result += s[mid]

        return result