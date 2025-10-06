# 587 - https://leetcode.com/problems/permutation-in-string/

# Time: O(n)
# Space: O(1) - since there are only 26 lowercase letters

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if len(s1) == 0: return True
        if len(s2) == 0: return False

        hmS1, hmS2 = {}, {}
        for i in range(len(s1)):
            hmS1[s1[i]] = 1 + hmS1.get(s1[i], 0)
            hmS2[s2[i]] = 1 + hmS2.get(s2[i], 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if hmS1 == hmS2:
                return True
            
            # add right char
            hmS2[s2[right]] = 1 + hmS2.get(s2[right], 0)

            # remove left char
            hmS2[s2[left]] -= 1
            if hmS2[s2[left]] == 0:
                del hmS2[s2[left]]
            left += 1
        
        return hmS1 == hmS2