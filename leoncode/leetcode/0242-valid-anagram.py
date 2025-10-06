# 242 - https://leetcode.com/problems/valid-anagram/

# Time: O(N)
# Space: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        hmS = {}
        hmT = {}

        # populate hashmaps with character counts
        for i in range(n):
            hmS[s[i]] = 1 + hmS.get(s[i], 0)
            hmT[t[i]] = 1 + hmT.get(t[i], 0)
        
        return hmS == hmT
