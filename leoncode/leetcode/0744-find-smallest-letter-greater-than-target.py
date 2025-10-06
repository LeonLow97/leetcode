# 744 - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Time: O(log n) - binary search
# Space: O(1)

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