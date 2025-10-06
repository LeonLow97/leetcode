# 152 - https://leetcode.com/problems/maximum-product-subarray/

# Time: O(n) - we traverse the list once
# Space: O(1) - we use constant space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # If the numbers are all positive, the maximum product is the product of all numbers
        # If the numbers are all negative, it is more tricky as we could alternate between positive and negative products
        # The solution is to always maintain the current maximum and minimum product subarray
        curMax, curMin = 1, 1 # `1` is the neutral value
        res = max(nums)

        for num in nums:
            # edge case, reset to neutral value
            if num == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = num * curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num) # curMax has been overrided in previous line, hence using tmp variable

            res = max(res, curMax)

        return res