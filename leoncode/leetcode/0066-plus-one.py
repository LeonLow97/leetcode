# 66 - https://leetcode.com/problems/plus-one/

# Time: O(n)
# Space: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            
        return [1] + digits