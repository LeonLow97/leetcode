# 283 - https://leetcode.com/problems/move-zeroes/

# Optimal: Two Pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
