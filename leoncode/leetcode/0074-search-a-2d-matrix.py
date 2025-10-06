# 74 - https://leetcode.com/problems/search-a-2d-matrix/

# Time: O(log (r * c)) = O(log r + log c)
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        if target < matrix[top][0] or target > matrix[bottom][-1]:
            return False
        rowNum = None
        while top <= bottom:
            middle = top + (bottom - top) // 2
            
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                rowNum = middle
                break
            if target < matrix[middle][0]:
                bottom = middle - 1
            else:
                top = middle + 1
        
        if rowNum is None: return False

        left, right = 0, COLS - 1
        nums = matrix[rowNum]
        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return True
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False
