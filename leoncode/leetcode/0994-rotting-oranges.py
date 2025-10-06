# 994 - https://leetcode.com/problems/rotting-oranges/

# Time: O(ROWS * COLS)
# Space: O(ROWS * COLS)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            qLen = len(q)
            time += 1
            for _ in range(qLen):
                rotten_r, rotten_c = q.popleft()
                for dr, dc in directions:
                    r, c = rotten_r + dr, rotten_c + dc
                    if (0 <= r < ROWS and 0 <= c < COLS and
                        grid[r][c] == 1):
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))

        return time if fresh == 0 else -1