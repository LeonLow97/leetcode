# 49 - https://leetcode.com/problems/group-anagrams/

# Time: O(N * KlogK) where N is the number of strings and K is the maximum length of a string
# Space: O(N * K)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # key --> sorted str, value --> array of strings

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hm:
                hm[sorted_s] = []
            hm[sorted_s].append(s)

        res = []
        for value in hm.values():
            res.append(value)
        return res
