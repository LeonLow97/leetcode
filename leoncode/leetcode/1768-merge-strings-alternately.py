# 1768 - https://leetcode.com/problems/merge-strings-alternately/

# Optimal: One Pointer
# Time: O(n + m) 
# Space: O(n + m) where n is len(word1) and m is len(word2)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []

        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        if i < len(word1):
            res.append(word1[i:])
        if i < len(word2):
            res.append(word2[i:])

        return ''.join(res)
