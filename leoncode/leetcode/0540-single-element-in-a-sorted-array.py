# 540 - https://leetcode.com/problems/single-element-in-a-sorted-array/

# Time: O(log n)
# Space: O(1)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            # Check if middle index is odd
            # Reason is because we want to compare the first element in a pair
            # E.g., [1,1,2,2,3,3,4,8,8], our pairs will be (1,1), (2,2), (3,3)
            # the first element in each pair is an even index, i.e., index 0, 2, 4

            # When the pair is disrupted with single element --> (4, 8), we observe that
            # the first element is not equal to second element, thus the search will be on the
            # right side of the array inclusive of the middle element
            # single element is always the first element of a pair

            if middle % 2 == 1:
                middle -= 1

            if nums[middle] == nums[middle + 1]:
                # if this condition is true, the left portion is valid, 
                # so the single element must be on the right of middle
                left = middle + 2
            else:
                right = middle

        return nums[left]
