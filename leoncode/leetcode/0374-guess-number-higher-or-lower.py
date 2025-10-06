# 374 - https://leetcode.com/problems/guess-number-higher-or-lower/

# Time: O(log n)
# Space: O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            middle = left + (right - left) // 2

            guessNum = guess(middle)

            if guessNum == 0:
                return middle
            
            if guessNum == -1:
                right = middle - 1
            elif guessNum == 1:
                left = middle + 1
