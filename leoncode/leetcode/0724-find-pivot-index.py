# 724 - https://leetcode.com/problems/find-pivot-index/

# Time: O(n)
# Space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # base case
        if not nums: return -1
        if len(nums) == 1: return 0

        sum = 0
        for i in nums: 
            sum += i

        leftSum = 0
        rightSum = sum

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1