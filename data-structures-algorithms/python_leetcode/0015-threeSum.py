'''
Difficulty: MEDIUM
No.15    https://leetcode.com/problems/3sum/
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
            
        # Sort the array
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = len(nums) - 1
            left = i + 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if tempSum < 0:
                    left += 1
                elif tempSum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
                
        return result
    
S = Solution()
print(S.threeSum([0,1,1]))
print(S.threeSum([-1,0,1,2,-1,-4]))
print(S.threeSum([0,0,0,0]))

