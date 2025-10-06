# 59 - https://leetcode.com/problems/spiral-matrix-ii/

# Time: O(n^2)
# Space: O(1) (not counting the output matrix)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # base case
        if n == 1: return [[1]]

        # generate matrix and pointers
        # arr = [[0] * n] * n
        arr = [[0 for j in range(n)] for i in range(n)]
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