/*
Difficulty: EASY
No.26    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the 
result be placed in the first part of the array nums. More formally, if there are k elements after removing 
the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
*/

// My Solution (~200ms)
var removeDuplicates = function(nums) {
    if (nums.length < 1) return nums.length;

    // set left and right pointers (right pointer moves to check for duplicates to the left element)
    let left = 0;
    let right = left + 1;

    while (left < nums.length) {
        if (right < nums.length) {
            if (nums[left] === nums[right]) {
                nums.splice(right, 1);
            } else {
                right++
            }
        } else {
            left++;
            right = left + 1;
        }
    }
    console.log("array: ", nums)
    return nums.length;
}

console.log(removeDuplicates([1,1,2]))  // 2
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  // 5

// Tutor's Solution (~130ms)
var swap = function(arr, idx1, idx2) {
    var temp = arr[idx1];
    arr[idx1] = arr[idx2]
    arr[idx2] = temp;
}

// Tutor's Solution (~130ms)
var removeDuplicatesRefactored = function(nums) {
    // base case
    if (nums.length < 1) return false;

    // define pointers
    let L = 0;
    let R = 1;

    while (R < nums.length) {
        if (nums[L] === nums[R]) {
            R++;
        // remove duplicates
        } else if (nums[L] !== nums[R]) {
            swap(nums, L+1, R)
            L++;
            R++;
        }
    }
    return L+1
}

console.log(removeDuplicatesRefactored([1,1,2])) // 2 
console.log(removeDuplicatesRefactored([0,0,1,1,1,2,2,3,3,4])) // 5

