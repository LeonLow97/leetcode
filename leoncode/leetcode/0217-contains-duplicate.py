# 217 - https://leetcode.com/problems/contains-duplicate/

# Time: O(n)
# Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False
