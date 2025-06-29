'''
Difficulty: Easy
No.463    https://leetcode.com/problems/island-perimeter/
'''

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        # depth first search
        def dfs(r, c):
            perimeter = 0

            # base case (adding 1 to perimeter)
            ## Case 1: position is out of range
            ## Case 2: position is in the water
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            if (r, c) in visited: 
                return 0

            visited.add((r,c))

            perimeter += dfs(r + 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c - 1)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)