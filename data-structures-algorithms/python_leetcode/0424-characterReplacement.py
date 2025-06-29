'''
Difficulty: MEDIUM
No.424    https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character
of the string and change it to any other uppercase English character. You 
can perform this operation at most k times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # base case
        if len(s) < k+1: return k+1

        # define sliders
        left = 0
        right = 0

        # define char and maxLen and hashmap
        maxLen = -float('inf')
        char = ""
        freqCounter = {}

        while right < len(s):
            if s[right] not in freqCounter:
                freqCounter[s[right]] = 1
            else:
                freqCounter[s[right]] += 1

            # determine the number of replaced characters
            mostFreq = max(freqCounter.values())
            currentLen = right - left + 1
            replacedChar = currentLen - mostFreq

            if replacedChar > k:
                freqCounter[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right-left+1)
            right += 1

        return maxLen if maxLen != -float('inf') else 0

S = Solution()
print(S.characterReplacement("ABAB", 2)) # 4. Replace the two 'A's with two 'B's or vice versa
print(S.characterReplacement('AABABBA', 1)) # 4 'BBBB'