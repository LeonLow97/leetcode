# 50 - https://leetcode.com/problems/powx-n/

# Time: O(log n)
# Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if x == 0: return 0
        if x == 1: return 1

        isNegativeExp = False
        if n < 0:
            isNegativeExp = True
            n = abs(n)
        
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            x *= x
            n //= 2

        return 1 / res if isNegativeExp else res
