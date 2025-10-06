# 200 - https://leetcode.com/problems/number-of-islands/

# Time: O(M * N) where M is the number of rows and N is the number of columns in the grid.
# Space: O(M * N) in the worst case where the grid is filled with lands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 0: return 0
        if COLS == 0: return 0

        res = 0
        visited = set()
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == "0"):
                return

            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res