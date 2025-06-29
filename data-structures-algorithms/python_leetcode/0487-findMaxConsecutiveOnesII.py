'''
Difficulty: MEDIUM
No.487    https://leetcode.com/problems/max-consecutive-ones-ii/

Given a binary array, find the maximum number of consecutive 1s in this array
if you can flip at most one 0.

Constraints:
- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.
'''

# Sliding Window Technique (Long winded)
def findMaxConsecutiveOnes(nums):
    # base case
    if (len(nums) < 2): return nums[0]

    # define pointers, counter and maxLen
    left = 0
    right = 0
    counter = 0
    maxLen = 0

    # find maxLen
    while (right < len(nums)):
        if (nums[right] == 1):
            if (right == len(nums) - 1):
                maxLen = max(maxLen, right-left+1)
            right += 1
        elif (nums[right] == 0 and counter < 1):
            counter += 1
            if (right == len(nums) - 1):
                maxLen = max(maxLen, right-left+1)
            right += 1
        else:
            maxLen = max(maxLen, right-left)
            left = right + 1
            right = left

    # return maxLen
    return maxLen

print(findMaxConsecutiveOnes([1,1,0,1,1,1])) # 6
print(findMaxConsecutiveOnes([1,0,1,1,0])) # 4
print(findMaxConsecutiveOnes([1])) # 1
print()

# Tutor's Solution
def findMaxConsecutiveOnes2(nums):
    # base case
    if (len(nums) < 2): return 1

    # define pointers, maxLen, zeroCounter
    left = 0
    right = 0
    maxLen = 0
    zeroCounter = 0

    # find maxLen
    while (right < len(nums)):
        if (nums[right] == 0):
            zeroCounter += 1
        
        # contract window if we don't meet the condition
        while (zeroCounter > 1):
            if (nums[left] == 0):
                zeroCounter -= 1
            left += 1
        
        maxLen = max(maxLen, right-left+1)
        right += 1

    # return maxLen
    return maxLen

print(findMaxConsecutiveOnes2([1,1,0,1,1,1])) # 6
print(findMaxConsecutiveOnes2([1,0,1,1,0])) # 4
print(findMaxConsecutiveOnes2([1])) # 1
