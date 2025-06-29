'''
Difficulty: Easy
No.977    https://leetcode.com/problems/squares-of-a-sorted-array/
'''

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      if len(nums) == 1: return [nums[0] * nums[0]]
      
      # define pointers
      result = []
      left = 0
      right = len(nums) - 1

      for i in range(len(nums)):
         leftSq = nums[left] * nums[left]
         rightSq = nums[right] * nums[right]
         if leftSq > rightSq:
            result.append(leftSq)
            left += 1
         else:
            result.append(rightSq)
            right -= 1

      return result[::-1]
        
          
S = Solution()
print(S.sortedSquares([-4,-1,0,3,10])) # [0,1,9,16,100]
print(S.sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]