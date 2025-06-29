'''
Difficulty: MEDIUM
No.763    https://leetcode.com/problems/partition-labels/
'''

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # base case
        if len(s) == 1: return [1]

        # Create a HashMap to determine the last index for each character in the string
        lastIndexHM = {}
        for idx, char in enumerate(s):
            lastIndexHM[char] = idx

        # define size and end
        idx = 0
        size = 0
        end = 0
        result = []

        for idx, char in enumerate(s):
            size += 1
            if lastIndexHM[char] > end:
                end = lastIndexHM[char]

            if idx == end:
                result.append(size)
                size = 0

        return result
    

S = Solution()
print(S.partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
print(S.partitionLabels("eccbbbbdec")) # [10]