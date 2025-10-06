# 81 - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Time: O(log n) on average, O(n) in the worst case
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return True

            # both ends equal, shrink both sides
            if nums[middle] == nums[left] and nums[middle] == nums[right]:
                left += 1
                right -= 1
                continue

            # Left half is sorted
            if nums[middle] > nums[right]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < nums[right]:
            # Right half is sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                right -= 1

        return False
