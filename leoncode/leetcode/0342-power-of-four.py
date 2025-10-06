# 342 - https://leetcode.com/problems/power-of-four/

# Time: O(log₄ n)
# Space: O(log₄ n) - recursion stack

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # edge case
        if n == 1:
            return True
        if n <= 0 or n % 4:
            return False

        return self.isPowerOfFour(n // 4)