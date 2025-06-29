'''
Difficulty: MEDIUM
No.59    https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # base case
        if n == 1: return [[1]]

        # generate matrix of n x n
        arr = []
        for i in range(n):
            row = [0] * n
            arr.append(row)

        # define borders
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        num = 0

        while True:
            for i in range(left, right + 1):
                num += 1
                arr[top][i] = num
            top += 1
            if left > right or top > bottom: break

            for i in range(top, bottom + 1):
                num += 1
                arr[i][right] = num
            right -= 1
            if left > right or top > bottom: break

            for i in range(right, left - 1, -1):
                num += 1
                arr[bottom][i] = num
            bottom -= 1
            if left > right or top > bottom: break

            for i in range(bottom, top - 1, -1):
                num += 1
                arr[i][left] = num
            left += 1
            if left > right or top > bottom: break

        return arr

S = Solution()
n = 3
print(S.generateMatrix(n)) # [[1,2,3],[8,9,4],[7,6,5]]
n = 1
print(S.generateMatrix(n)) # [[1]]
n = 5
print(S.generateMatrix(n)) # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]