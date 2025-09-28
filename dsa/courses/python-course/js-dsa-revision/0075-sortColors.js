/*
Difficulty: MEDIUM
No.75    https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Constraints:

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.
*/

var swap = function (arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
};

var sortColors = function (arr) {
  if (arr.length === 1 || arr.length === 0) return arr;

  let left = 0;
  let right = 0;

  while (right < arr.length) {
    if (arr[right] === 0) {
      swap(arr, left, right);
      left++;
      right++;
    } else {
      right++;
    }
  }

  right = left;
  while (right < arr.length) {
    if (arr[right] == 1) {
      swap(arr, left, right);
      left++;
      right++;
    } else {
      right++;
    }
  }
  return arr;
};
// [0,0,2,1,1,2]
console.log(sortColors([2, 0, 2, 1, 1, 0])); // [0,0,1,1,2,2]
console.log(sortColors([2, 0, 1])); // [0,1,2]
