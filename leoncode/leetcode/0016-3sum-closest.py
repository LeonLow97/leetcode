# 16 - https://leetcode.com/problems/3sum-closest/

# Time Complexity: O(n^2)
# Space Complexity: O(1)
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