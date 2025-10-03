# 18 - https://leetcode.com/problems/4sum/

# Optimal: Two Pointers
# Time: O(n^3)
# Space: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # O(n log n)
        res = []
        i, j = 0, 0

        for i in range(len(nums)):
            if 0 < i and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums)):
                if i+1 < j and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
