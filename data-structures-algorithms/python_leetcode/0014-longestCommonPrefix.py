'''
Difficulty: Easy
No.14    https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        # strs[0] might not be the shortest string, so use i == len(s) condition to check if it went out of bounds
        for i in range(len(strs[0])):
            for s in strs:
                # 2 scenarios to return: we find a shorter string or the next prefix is not the same
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res



S = Solution()
strs = ["flower","flow","flight"]
print(S.longestCommonPrefix(strs)) # "fl"
