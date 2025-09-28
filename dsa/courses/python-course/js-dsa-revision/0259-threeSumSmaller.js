/*
Difficulty: MEDIUM
No.15    https://leetcode.com/problems/3sum-smaller/

Given an array of n integers nums and an integer target, find the number
of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
nums[i] + nums[j] + nums[k] < target.

Constraints:

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
*/

// Runtime (3ms)
// Got this question wrong. (did not do count += right -  left for faster runtime)
var threeSumSmaller = function (nums, target) {
  // sort the array
  nums.sort(function (a, b) {
    return a - b;
  });

  // define counter
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let currentSum = nums[i] + nums[left] + nums[right];
      if (currentSum < target) {
        count += right - left;
        left++;
      } else {
        right--;
      }
    }
  }
  return count;
};

console.log(threeSumSmaller([-2, 0, 1, 3], 2)); // 2 because of 2 triplets [-2,0,1] and [-2,0,3]
console.log(threeSumSmaller([-2, 0, 1, 3, 5], 3)); // 3
console.log(threeSumSmaller([], 0)); // output 0
console.log(threeSumSmaller([0], 0)); // output 0
