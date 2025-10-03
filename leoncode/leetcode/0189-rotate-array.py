# 189 - https://leetcode.com/problems/rotate-array/

# Brute Force
# Time: O(n)
# Space: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0] * n

        k = k % n # k can be greater than n

        for i in range(n):
            num = nums[i]
            i = (i + k) % n # not super intuitive but it is to get the next position after rotation
            res[i] = num

        nums[:] = res

# Optimal: Two Pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def two_pointer(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # reverse the array without using extra space using 2 pointers
        left, right = 0, n-1
        two_pointer(nums, left, right)
        
        # reverse the first portion
        left, right = 0, k-1
        two_pointer(nums, left, right)

        # reverse the second portion
        left, right = k, n-1
        two_pointer(nums, left, right)
