# 76 - https://leetcode.com/problems/minimum-window-substring/

# Time: O(N) where N is the length of string s
# Space: O(1) since the hashmaps will contain at most 52 characters (
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmS, hmT = {}, {}

        for char in t:
            hmT[char] = 1 + hmT.get(char, 0)

        left = 0
        resL, resR = 0, len(s) + 1
        have, need = 0, len(hmT)

        for right in range(len(s)):
            char = s[right]
            hmS[char] = 1 + hmS.get(char, 0)
            if char in hmT and hmS[char] == hmT[char]:
                have += 1

            while have == need:
                # compute current min window substring
                if (right-left+1) < (resR-resL+1):
                    resL, resR = left, right
                
                hmS[s[left]] -= 1
                if s[left] in hmT and hmS[s[left]] < hmT[s[left]]:
                    have -= 1
                left += 1
        
        return s[resL:resR+1] if resR != len(s)+1 else ""