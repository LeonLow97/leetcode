# 13 - https://leetcode.com/problems/roman-to-integer/

# Time: O(n) where n is the length of the input string.
# Space: O(1)
class Solution:
    def romanToInt(self, str):
        value = 0
        if "IV" in str: 
            value += 4
            str = str.replace("IV", "")
        if "IX" in str: 
            value += 9
            str = str.replace("IX", "")
        if "XL" in str: 
            value += 40
            str = str.replace("XL", "")
        if "XC" in str: 
            value += 90
            str = str.replace("XC", "")
        if "CD" in str: 
            value += 400
            str = str.replace("CD", "")
        if "CM" in str: 
            value += 900
            str = str.replace("CM", "")

          ## converting string to value
        if "M" in str:
            numM = str.count("M")
            value += 1000 * numM
            str = str.replace("M", "")
        if "D" in str:
            numD = str.count("D")
            value += 500 * numD
            str = str.replace("D", "")
        if "C" in str:
            numC = str.count("C")
            value += 100 * numC
            str = str.replace("C", "")
        if "L" in str:
            numL = str.count("L")
            value += 50 * numL
            str = str.replace("L", "")
        if "V" in str:
            numV = str.count("V")
            value += 5 * numV
            str = str.replace("V", "")
        if "X" in str:
            numX = str.count("X")
            value += 10 * numX
            str = str.replace("X", "")
        if "I" in str:
            numI = str.count("I")
            value += 1 * numI
            str = str.replace("I", "")

        return value