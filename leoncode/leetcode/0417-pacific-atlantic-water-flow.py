# 417 - https://leetcode.com/problems/pacific-atlantic-water-flow/

# Time: O(ROWS * COLS)
# Space: O(ROWS * COLS)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r, c, prevHeight, visited):
            if (
                r < 0 or r >= ROWS or c < 0 or c >= COLS or
                heights[r][c] < prevHeight or
                (r, c) in visited
                ):
                return

            visited.add((r, c))

            dfs(r+1, c, heights[r][c], visited)
            dfs(r-1, c, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)

        for r in range(ROWS):
            dfs(r, 0, -1, pacific)
            dfs(r, COLS - 1, -1, atlantic)

        for c in range(COLS):
            dfs(0, c, -1, pacific)
            dfs(ROWS - 1, c, -1, atlantic)

        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])

        return res 