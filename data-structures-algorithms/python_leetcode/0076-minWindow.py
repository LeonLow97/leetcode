'''
Difficulty: HARD
No.76    https://leetcode.com/problems/minimum-window-substring/
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # define sliders
        left = 0
        right = 0
        minWindow = ""
        minLen = float('inf')
        counter = 0

        # define hashmap to store character count of t
        freqCounter = {}
        for char in t:
            if char not in freqCounter:
                freqCounter[char] = 1
            else:
                freqCounter[char] += 1

        while right < len(s):
            if s[right] in freqCounter:
                freqCounter[s[right]] -= 1
                if freqCounter[s[right]] >= 0:
                    counter += 1

            while counter == len(t):
                currentLen = right - left + 1
                if currentLen < minLen:
                    minWindow = s[left:right+1]
                    minLen = currentLen
                
                if s[left] in freqCounter:
                    freqCounter[s[left]] += 1
                    if freqCounter[s[left]] > 0:
                        counter -= 1
                left += 1
            
            right += 1

        return minWindow if minLen != float('inf') else ""

S = Solution()
print(S.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(S.minWindow("a", "a")) # "a"
print(S.minWindow("a", "aa")) # ""