'''
Difficulty: MEDIUM
No.54    https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.
'''

from typing import List

# My Solution
# Runtime: 26ms, Memory: 13.8 MB
# Time complexity: O(mn), space complexity: O(mn)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # base case
        if not matrix: return []
        
        # define size of matrix
        rows = len(matrix)
        cols = len(matrix[0])
        arr = []

        # define row and col, and idx
        rowStart, colStart = 0, 0
        rowEnd, colEnd = rows - 1, cols - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # rightwards
            for col in range(colStart, colEnd + 1):
                arr.append(matrix[rowStart][col])
            rowStart += 1

            # downwards
            for row in range(rowStart, rowEnd + 1):
                arr.append(matrix[row][colEnd])
            colEnd -= 1

            # leftwards
            # starting row > rowEnd means there are no more rows left to traverse
            if rowStart <= rowEnd:
                for col in range(colEnd, colStart - 1, -1):
                    arr.append(matrix[rowEnd][col])
                rowEnd -= 1

            # upwards
            if colStart <= colEnd:
                for row in range(rowEnd, rowStart - 1, -1):
                    arr.append(matrix[row][colStart])
                colStart += 1

        return arr

S = Solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]] # [1,2,3,6,9,8,7,4,5]
print(S.spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(S.spiralOrder(matrix)) # [1,2,3,4,8,12,11,10,9,5,6,7]

# Eric's Solution
# Runtime: 22ms, Memory 13.8 MB
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while True:
            for i in range(left, right + 1):
                arr.append(matrix[top][i])
            top += 1
            if left > right or top > bottom: break

            for i in range(top, bottom + 1):
                arr.append(matrix[i][right])
            right -= 1
            if left > right or top > bottom: break

            for i in range(right, left - 1, -1):
                arr.append(matrix[bottom][i])
            bottom -= 1
            if left > right or top > bottom: break

            for i in range(bottom, top - 1, -1):
                arr.append(matrix[i][left])
            left += 1
            if left > right or top > bottom: break
        
        return arr

S = Solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]] # [1,2,3,6,9,8,7,4,5]
print(S.spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(S.spiralOrder(matrix)) # [1,2,3,4,8,12,11,10,9,5,6,7]