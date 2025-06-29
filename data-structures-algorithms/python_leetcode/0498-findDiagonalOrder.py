'''
Difficulty: MEDIUM
No.498    https://leetcode.com/problems/diagonal-traverse/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Questions
- Is it always going to be a square matrix?
- If it is an empty matrix (size 0), should we return [], an empty list?
'''

from typing import List

# My Solution
# Runtime: 197ms, Memory: 18 MB
# Time complexity: O(mn), Space Complexity: O(mn)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # base case
        if not mat: return []

        # get the length of the list
        size = len(mat)

        # define start, result, backward and counter
        start = 0
        counter = 1 # number of elements to append into result
        result = []
        backward = True
        pos = 0

        # iterate through the list
        while start != size:
            for i in range(start, counter):
                first = mat[i].pop(0)
                if not backward:
                    result.append(first)
                elif backward:
                    result.insert(pos, first)

            pos += counter - start

            if not mat[0]:
                start += 1

            if counter < size: 
                counter += 1

            backward = not backward
            
        return result

S = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]] # [1,2,4,7,5,3,6,8,9]
print(S.findDiagonalOrder(mat))
mat = [[1,2],[3,4]]
print(S.findDiagonalOrder(mat)) # [1,2,3,4]

# Youtube's Solution
# https://www.youtube.com/watch?v=NTF7sDU0IWA&ab_channel=AlgorithmsMadeEasy
# To move in the upward direction, Row-- Column++
# When column is the last row, Row++, Column--
# Runtime: 193 ms, Memory: 17.8 MB
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # base case
        if not mat: return []

        # define size of matrix
        m = len(mat) # number of rows
        n = len(mat[0]) # number of columns

        # initialize arr with size m * n
        arr = [0] * (m * n)

        i = 0
        row, col = 0, 0
        upwards = True

        while row < m and col < n:
            # if diagonal is going upwards
            if upwards:
                while row > 0 and col < n - 1:
                    arr[i] = mat[row][col]
                    i += 1
                    row -= 1
                    col += 1
                arr[i] = mat[row][col]
                i += 1
                if col == n - 1:
                    row += 1
                else: 
                    col += 1

            # if diagonal is going downwards
            else:
                while col > 0 and row < m - 1:
                    arr[i] = mat[row][col]
                    i += 1
                    row += 1
                    col -= 1
                arr[i] = mat[row][col]
                i += 1
                if row == m - 1:
                    col += 1
                else:
                    row += 1

            upwards = not upwards

        return arr


        
