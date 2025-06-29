'''
Difficulty: MEDIUM
No.15    https://leetcode.com/problems/3sum-closest/
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # base case
        if len(nums) == 3: return sum(nums)

        # sort the array
        nums.sort()
        result = float('inf')

        for i in range(len(nums)):
            # define pointers
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                diff = abs(tempSum - target)

                if diff < abs(result - target):
                    result = tempSum

                if diff != 0:
                    if tempSum < target:
                        left += 1
                    if tempSum > target: 
                        right -= 1
                else:
                    return tempSum
                
        return result


S = Solution()
print(S.threeSumClosest([-1,2,1,-4], 1)) # 2 (-1 + 2 + 1)
print(S.threeSumClosest([0,0,0], 1)) # 0
print(S.threeSumClosest([1,1,1,1], 3)) # 3
print(S.threeSumClosest([1,1,1,1], 4)) # 3