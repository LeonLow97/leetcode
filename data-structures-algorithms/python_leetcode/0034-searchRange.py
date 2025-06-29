'''
Difficulty: MEDIUM
No.34    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Constraints:

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array.
- -10^9 <= target <= 10^9
'''

# Some good questions to ask the interviewer for this question
# if the target only appeared once, do we return [idx] or [idx, idx]?
# how many duplicate values can we have in the array? it seems that the given examples on leetcode only has 2 duplicate values.

def searchRange(nums, target):
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

    if (nums[left] == target): return left # account for the case where nums=[3,3,3]
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

print(searchRange([5,7,7,8,8,10], 8)) # [3,4]
print(searchRange([5,7,7,8,8,10], 6)) # [-1,-1]
print(searchRange([], 0)) # [-1,-1]
print(searchRange([1,3], 3)) # [1,1]
print(searchRange([3,3,3], 3)) # [0,2]