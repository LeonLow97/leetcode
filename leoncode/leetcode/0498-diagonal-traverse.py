# 498 - https://leetcode.com/problems/diagonal-traverse/

# Time: O(M * N) where M is number of rows and N is number of columns
# Space: O(1) ignoring output array

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        noOfElements = ROWS * COLS

        res = []

        cur_row, cur_col = 0, 0

        # up direction : up --> right
        # down direction: down --> left
        going_up = True

        while len(res) != noOfElements:
            if going_up:
                while cur_row >= 0 and cur_col < COLS:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                
                # pointer is now out of bounds, need to bring it back
                if cur_col == COLS: # at out of bounds '3', need to bring it back to '6
                    cur_row += 2
                    cur_col -= 1
                else: # at out of bounds above '2', need to bring it back to '2'
                    cur_row += 1

                going_up = False
            else:
                while cur_col >= 0 and cur_row < ROWS:
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                
                # pointer is now out of bounds, need to bring it back
                if cur_row == ROWS:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1

                going_up = True

        return res