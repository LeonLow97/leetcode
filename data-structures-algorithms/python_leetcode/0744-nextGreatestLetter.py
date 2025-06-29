'''
Difficulty: EASY
No.744    https://leetcode.com/problems/find-smallest-letter-greater-than-target/

You are given an array of characters letters that is sorted in non-decreasing order, 
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Constraints:

- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter.
- letters is sorted in non-decreasing order.
- letters contains at least two different characters.
- target is a lowercase English letter.
'''

from typing import List

class Solution:
     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
          # define binary pointers
          left = 0
          right = len(letters) - 1

          # BASE CASE
          if (letters[right] <= target or letters[left] > target): return letters[0]

          while left < right:
                middle = left + (right - left) // 2
                if (letters[middle] > target):
                     right = middle
                else:
                     left = middle + 1
                     
          return letters[left]
                  

S = Solution()
print(S.nextGreatestLetter(["c","f","j"], "a")) # "c"
print(S.nextGreatestLetter(["c","f","j"], "c")) # "f"
print(S.nextGreatestLetter(["c","f","j"], "j")) # "c"
print(S.nextGreatestLetter(["c","f","j"], "k")) # "c"
print(S.nextGreatestLetter(["x","x","y","y"], "z")) # "x"