# 73 - https://leetcode.com/problems/set-matrix-zeroes/

# Time: O(M * N)
# Space: O(M + N)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        zeroes = []
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroes.append((r, c))

        for r, c in zeroes:
            if matrix[r][c] == 0:
                # entire row converted to 0
                for i in range(COLS):
                    matrix[r][i] = 0
                
                # entire col converted to 0
                for i in range(ROWS):
                    matrix[i][c] = 0