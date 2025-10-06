# 36 - https://leetcode.com/problems/valid-sudoku/

# Time: O(N^2) where N is the number of rows or columns (9 in this case)
# Space: O(N) for the sets used to track seen numbers
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            rowsSet = set()
            for c in range(COLS):
                char = board[r][c]
                if char != ".":
                    if char in rowsSet: return False
                    rowsSet.add(char)

        for c in range(COLS):
            colsSet = set()
            for r in range(ROWS):
                char = board[r][c]
                if char != ".":
                    if char in colsSet: return False
                    colsSet.add(char)

        for boxR in range(3):
            for boxC in range(3):
                boxSet = set()
                for r in range(boxR * 3, boxR * 3 + 3):
                    for c in range(boxC * 3, boxC * 3 + 3):
                        char = board[r][c]
                        if char != ".":
                            if char in boxSet: return False
                            boxSet.add(char)

        return True