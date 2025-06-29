## Issue with Time Limit Exceeded: https://stackoverflow.com/questions/74583208/python-leetcode-3-time-limit-exceeded?noredirect=1#comment131660903_74583208
'''
Difficulty: MEDIUM
No.3    https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case
        if len(s) < 2: return len(s) 

        # define sliders, maxLen, and hashmap
        left = 0
        right = 0
        maxLen = -float('inf')
        freqCounter = {}

        while right < len(s):
            if s[right] in freqCounter:
                freqCounter[s[right]] += 1
            else:
                freqCounter[s[right]] = 1

            rightChar = s[right]

            # eliminate repeated characters by moving left slider
            while freqCounter[rightChar] > 1:
                freqCounter[s[left]] -= 1
                if freqCounter[s[left]] == 0:
                    del freqCounter[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        if maxLen == -float('inf'): return 0
        return maxLen

S = Solution()
print(S.lengthOfLongestSubstring("abcabcbb")) # 3 'abc'
print(S.lengthOfLongestSubstring("bbbbb")) # 1 'b'
print(S.lengthOfLongestSubstring("pwwkew")) # 3 'wke'
print(S.lengthOfLongestSubstring("")) # 0 ''
