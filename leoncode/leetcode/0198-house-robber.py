# 198 - https://leetcode.com/problems/house-robber/

# Time: O(n)
# Space: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for num in nums:
            temp = two
            two = max(num + one, two)
            one = temp

        return two