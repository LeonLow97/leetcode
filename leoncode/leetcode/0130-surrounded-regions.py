# 130 - https://leetcode.com/problems/surrounded-regions/

# Time: O(N * M) where N is number of rows and M is number of columns
# Space: O(N * M) in the worst case for the recursion stack
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                board[r][c] == "X" or board[r][c] == "U"):
                return

            board[r][c] = "U"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "U":
                    board[r][c] = "O"