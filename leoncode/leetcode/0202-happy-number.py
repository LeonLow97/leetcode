# 202 - https://leetcode.com/problems/happy-number/

# Time: O(log n)
# Space: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            temp = 0
            for digit in str(n):
                temp += int(digit) ** 2
            n = temp
            if n == 1:
                return True

        return False