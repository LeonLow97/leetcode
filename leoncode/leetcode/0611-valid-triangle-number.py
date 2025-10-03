# 611 - https://leetcode.com/problems/valid-triangle-number/

# Optimal: Two Pointers
# Time: O(n^2)
# Space: O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        
        return res
