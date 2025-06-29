'''
Difficulty: Easy
No.118    https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # base case
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]

        result = [[1], [1,1]]
        prev = [1,1]

        for row in range(3, numRows + 1):
            sub = [0] * row
            leftIdx = 0
            rightIdx = row - 1
            sub[leftIdx] = 1
            sub[rightIdx] = 1

            while leftIdx < rightIdx:
                subSum = prev[leftIdx] + prev[leftIdx + 1]
                leftIdx += 1
                rightIdx -= 1
                sub[leftIdx] = subSum
                sub[rightIdx] = subSum

            prev = sub
            result.append(sub)

        return result

S = Solution()
print(S.generate(5))
S = Solution()
print(S.generate(10))
S = Solution()
print(S.generate(1))

# Eric's Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # define result and pre
        result = []
        pre = []
        pre.append(1)
        result.append(pre)

        for i in range(1, numRows):
            sub = []
            sub.append(1)
            for j in range(1, i):
                val = pre[j] + pre[j - 1]
                sub.append(val)
            sub.append(1)
            result.append(sub)
            pre = sub

        return result



        
                


                




