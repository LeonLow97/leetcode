# 695 - https://leetcode.com/problems/max-area-of-island/

# Time: O(ROWS * COLS)
# Space: O(ROWS * COLS)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            # base case
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0

            # found water
            visited.add((r, c))
            water = 1

            water += dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return water

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    res = max(res, area)
            
        return res
