'''
Difficulty: EASY
No.724    https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Questions to ask:
- If the list is empty, should I return -1?
- If the list only has 1 element, should I return 0?
'''

from typing import List

# My Solution
# Runtime: 160ms, Memory: 15.2 MB
# Time Complexity: O(N), Space Complexity: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # base case
        if not nums: return -1
        if len(nums) == 1: return 0

        # define size of list and counter
        size = len(nums)
        counter = 0

        # define leftSum and rightSum
        leftSum = 0
        rightSum = sum(nums[counter + 1: size])

        if leftSum == rightSum: return counter

        while counter != size:
            leftSum += nums[counter]
            counter += 1
            if counter == size:
                return -1
            rightSum -= nums[counter]

            if leftSum == rightSum:
                break

        return counter

S = Solution()
nums = [1,7,3,6,5,6] # 3
print(S.pivotIndex(nums))
nums = [1,2,3] # -1
print(S.pivotIndex(nums))
nums = [2,1,-1] # 0
print(S.pivotIndex(nums))

# Eric's Solution 
# Runtime: 157 ms, Space Complexity: 15.3 MB
# Time Complexity: O(N), Space Complexity: O(1)
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

