# 51 - https://leetcode.com/problems/n-queens/

# Time: O(N!) - we have N options for the first row, N-2 for the second (we can't place in the same column or diagonals), N-4 for the third, and so on.
# Space: O(N^2) - board of size N x N
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []

        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                board_copy = ["".join(row) for row in board]
                res.append(board_copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res
