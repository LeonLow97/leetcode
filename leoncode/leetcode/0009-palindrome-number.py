# 9 - https://leetcode.com/problems/palindrome-number/

# Time: O(n) where n is the number of digits in the integer.
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        left = 0
        right = len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            
            left += 1
            right -= 1

        return True
