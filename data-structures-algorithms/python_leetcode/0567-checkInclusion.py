'''
Difficulty: MEDIUM
No.567    https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # define window, counter, maxLen and freqCounter
        left = 0
        right = 0
        counter = 0
        foundS1Char = float('inf')
        freqCounter = {}

        # Use hashmap to store s1 characters
        for char in s1:
            if char not in freqCounter:
                freqCounter[char] = 1
            else:
                freqCounter[char] += 1

        while right < len(s2):
            if s2[right] in freqCounter:
                freqCounter[s2[right]] -= 1
                if freqCounter[s2[right]] >= 0:
                    counter += 1

            # contract window because all characters in s1 have been found
            while counter == len(s1):
                foundS1Char = min(foundS1Char, right - left + 1)

                if s2[left] in freqCounter:
                    freqCounter[s2[left]] += 1
                    if freqCounter[s2[left]] > 0:
                        counter -= 1
                left += 1
            
            right += 1

        return foundS1Char == len(s1)

S = Solution()
print(S.checkInclusion("ab", "adb")) # False
print(S.checkInclusion("ab", "eidbaooo")) # True. s2 contains one permutation of s1 ("ba")
print(S.checkInclusion("ab", "eidboaoo")) # False
print(S.checkInclusion("adc", "dcda")) # True