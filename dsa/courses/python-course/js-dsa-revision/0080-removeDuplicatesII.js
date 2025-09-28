/*
Difficulty: MEDIUM
No.80    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the 
result be placed in the first part of the array nums. More formally, if there are k elements after removing 
the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

- 1 <= nums.length <= 3 * 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.
*/

var swap = function(arr, idx1, idx2) {
    var temp = arr[idx1];
    arr[idx1] = arr[idx2]
    arr[idx2] = temp;
}

var removeDuplicates = function(nums) {
    // base case
    if (nums.length < 3) return nums.length;
    
    // define pointers and counter
    let L = 0;
    let R = 1;

    let counter = 0;

    // remove duplicates
    while (R < nums.length) {
        if (nums[L] !== nums[R]) {
            L++;
            nums[L] = nums[R]
            counter = 0;
        } else if (nums[L] == nums[R] && counter < 1) {
            counter++;
            L++
            nums[L] = nums[R]
        }
        R++;
    }
    // console.log(nums)
    return L + 1
}

console.log(removeDuplicates([1,1,2,2,2,3])) // 5
console.log(removeDuplicates([0,0,1,1,1,1,2,3,3])) // 7