# 424 - https://leetcode.com/problems/longest-repeating-character-replacement/

# Time: O(N)
# Space: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        hm = {}
        res = 0

        left = 0
        for right in range(len(s)):
            hm[s[right]] = 1 + hm.get(s[right], 0)
            maxFreq = max(maxFreq, hm[s[right]])

            while (right - left + 1) - maxFreq > k:
                hm[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res