'''
Difficulty: Medium
No.238    

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and **without using the division operation**.
'''

from typing import List

# Eric's Solution
# Time Complexity: O(n), Space Complexity: O(n)
# Runtime: 239ms, Memory: 22.4 MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        # define prefix and postfix
        prefix = [1] * n
        postfix = [1] * n
        result = []

        # populating prefix
        for i in range(n):
            # first element
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]

        # populating postfix
        for i in range(n - 1, -1, -1):
            # last element
            if i == n - 1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i + 1] * nums[i + 1]

        # populating result array
        for i in range(n):
            result.append(prefix[i] * postfix[i])

        return result

S = Solution()
nums = [1,2,3,4]
print(S.productExceptSelf(nums)) # [24,12,8,6]
nums = [-1,1,0,-3,3]
print(S.productExceptSelf(nums)) # [0,0,9,0,0]

# Eric's 2nd Solution (no postfix array required, used variable instead)
# Runtime: 237 ms, Memory: 21.3 MB
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        # populate prefix
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        # get product array except self
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

S = Solution()
nums = [1,2,3,4]
print(S.productExceptSelf(nums)) # [24,12,8,6]
nums = [-1,1,0,-3,3]
print(S.productExceptSelf(nums)) # [0,0,9,0,0]