# 15 - https://leetcode.com/problems/3sum/

# Optimal: Two Pointers
# Time: O(n^2) outer loop O(n) + inner two pointer O(n)
# Space: O(1), might be O(n) depending on sort implementation
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        current = 0
        res = []
        nums.sort() # O(n log n)

        while current < len(nums):
            while 0 < current < len(nums) and nums[current] == nums[current - 1]:
                current += 1
            
            left, right = current + 1, len(nums) - 1
            while left < right:
                total = nums[current] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[current], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
            current += 1
        
        return res
