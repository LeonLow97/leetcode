def findPeakElement(nums):
    # base case
    if nums[0] > nums[1]: return 0
    if nums[-1] > nums[-2]: return len(nums) - 1

    # define pointers
    left = 0
    right = len(nums) - 1

    while left < right: 
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else: 
            right = mid

    return left

print(findPeakElement([1,2,3,1])) # 2
print(findPeakElement([1,2,3,1,4])) # 4
print(findPeakElement([1,2,1,3,5,6,4])) # 5
print(findPeakElement([6,5,4,3,2,3,2])) # 0
print(findPeakElement([1,2,3,7,6,3,1])) # 3
print(findPeakElement([0,2,3,1,5,4,5])) # 6