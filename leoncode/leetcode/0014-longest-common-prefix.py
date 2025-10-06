# 14 - https://leetcode.com/problems/longest-common-prefix/

# Time: O(M * N) where M is the length of the shortest string and N is the number of strings
# Space: O(M) where M is the length of the shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        n = len(strs[0])

        for i in range(n):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        
        return res
