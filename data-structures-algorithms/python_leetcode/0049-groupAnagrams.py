'''
Difficulty: Medium
No.49    https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
'''

from typing import List
from collections import defaultdict

# Eric Programming
# Time complexity: O(m * nlogn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Define a defaultdict to group anagrams
        anagram_groups = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters of the string to get the key
            key = ''.join(sorted(s))
            
            # Add the string to the corresponding anagram group
            anagram_groups[key].append(s)
        
        # Convert the values of the defaultdict to a list and return it
        return list(anagram_groups.values())


# Neetcode
# Time complexity: O(mn), technically O(mn * 26)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case
        if len(strs) == 1: return [strs]

        # Mapping charCount to list of anagrams
        # defaultdict is when you try to access a key that does not exist,
        # it will create a new key with an empty list as its value.
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # use of tuples of keys because tuples are hashshable and can be used in hash map
            # lists on the other hand cannot be used as keys in a dictionary
            res[tuple(count)].append(s)

        return list(res.values())

S = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(S.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = [""]
print(S.groupAnagrams(strs)) # [[""]]
strs = ["a"]
print(S.groupAnagrams(strs)) # [["a"]]
strs = ["","",""]
print(S.groupAnagrams(strs)) # [["", "", ""]]

