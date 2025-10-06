# 34 - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        result = [-1,-1]

        # base case
        if (len(nums) == 0): return result

        leftIdx = findLeft(nums, target)
        rightIdx = findRight(nums, target)

        return [leftIdx, rightIdx]

def findLeft(nums, target):
    # define pointers
    left = 0
    right = len(nums) - 1

    while (left + 1 < right):
        mid = left + (right - left) // 2

        if (nums[mid] < target):
            left = mid
        else:
            right = mid

    if (nums[left] == target): return left
    elif (nums[right] == target): return right
    else: return -1

def findRight(nums, target):
    # define pointers
    left = 0
    right = len(nums) - 1

    while (left + 1 < right):
        mid = left + (right - left) // 2

        if (nums[mid] <= target):
            left = mid
        else:
            right = mid

    if (nums[right] == target): return right
    elif (nums[left] == target): return left
    else: return -1