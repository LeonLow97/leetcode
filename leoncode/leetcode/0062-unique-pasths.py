# 62 - https://leetcode.com/problems/unique-paths/

# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(r, c):
            # constraint
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in cache: return cache[(r, c)]

            pathRight = dfs(r + 1, c)
            pathDown = dfs(r, c + 1)

            cache[(r, c)] = pathRight + pathDown
            return cache[(r, c)]

        return dfs(0, 0)