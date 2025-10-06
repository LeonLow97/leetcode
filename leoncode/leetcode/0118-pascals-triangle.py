# 118 - https://leetcode.com/problems/pascals-triangle/

# Time: O(numRows^2)
# Space: O(numRows^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        res = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            temp = [1]

            for i in range(1, len(prev)):
                temp.append(prev[i-1] + prev[i])

            temp.append(1)
            res.append(temp)

        return res