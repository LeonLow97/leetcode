# 54 - https://leetcode.com/problems/spiral-matrix/

# Time: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space: O(1) - we are using only a constant amount of extra space.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS - 1
        top, bottom = 0, ROWS - 1

        res = []
        while True:
            # move to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if (left > right) or (top > bottom): break

            # move to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if (left > right) or (top > bottom): break

            # move to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if (left > right) or (top > bottom): break

            # move to top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if (left > right) or (top > bottom): break

        return res