# 70 - https://leetcode.com/problems/climbing-stairs/

# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if step in cache:
                return cache[step]

            one = dfs(step + 1)
            two = dfs(step + 2)

            cache[step] = one + two
            return cache[step]

        return dfs(0)