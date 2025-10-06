# 238 - https://leetcode.com/problems/product-of-array-except-self/

# Time: O(n)
# Space: O(1) (output array does not count as extra space)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res