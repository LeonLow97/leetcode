'''
Difficulty: MEDIUM
No.6    https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''

# My Solution (with some help from neetcode)
# Time complexity: O(n), Space complexity: O(n)
# Runtime: 67 ms, Memory: 14 MB
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

S = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(S.convert(s, numRows)) # "PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 4
print(S.convert(s, numRows)) # "PINALSIGYAHRPI"
s = "A"
numRows = 1
print(S.convert(s, numRows)) # "A"

