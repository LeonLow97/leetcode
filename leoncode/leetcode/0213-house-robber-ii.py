# 213 - https://leetcode.com/problems/house-robber-ii/

# Time: O(n)
# Space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.houseRobber(nums[0:-1]), self.houseRobber(nums[1:]))
        
    def houseRobber(self, houses):
        cache = {}

        def dfs(i):
            if i >= len(houses):
                return 0
            if i in cache:
                return cache[i]

            one = houses[i] + dfs(i + 2)
            two = dfs(i + 1)

            cache[i] = max(one, two)
            return cache[i]
        
        return dfs(0)