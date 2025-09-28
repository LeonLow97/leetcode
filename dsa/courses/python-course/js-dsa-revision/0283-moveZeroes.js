/*
Difficulty: EASY
No.283    https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Constraints:

- 1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
*/

// My Solution
var swap = function (arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
};

var moveZeroes = function (arr) {
  // left pointer is used to check if element is 0
  // right pointer looks for non-zero element
  let left = 0;
  let right = 1;

  while (right < arr.length) {
    if (arr[left] === 0) {
      if (arr[right] === 0) {
        right++;
      } else if (arr[right] !== 0) {
        swap(arr, left, right);
        left++;
        right++;
      }
    } else {
      left++;
      right++;
    }
  }
  return arr;
};

console.log(moveZeroes([0, 1, 0, 3, 12])); // [1,3,12,0,0]
console.log(moveZeroes([0])); // [0]
console.log(moveZeroes([1])); // [1]
console.log(moveZeroes([0, 0, 1])); // [1,0,0]
