'''
Difficulty: Medium
No.739    https://leetcode.com/problems/daily-temperatures/
'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # define stack (stack is in monotonic decreasing order)
        stack = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentT = temperatures[i]

            while stack and currentT > stack[-1][1]:
                stackIdx = stack.pop()[0]
                result[stackIdx] = i - stackIdx

            stack.append([i, currentT])            

        return result

S = Solution()
print(S.dailyTemperatures([73,74,75,71,69,72,76,73]))