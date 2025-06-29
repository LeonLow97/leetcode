/*
Difficulty: MEDIUM
No.15    https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Constraints:

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
*/

var threeSumClosest = function (arr, target) {
  if (arr.length === 3) {
    return arr[0] + arr[1] + arr[2];
  }

  arr.sort(function (a, b) {
    return a - b;
  });

  let sum = Infinity;
  let result;

  for (let i = 0; i < arr.length; i++) {
    let left = i + 1;
    let right = arr.length - 1;

    while (left < right) {
      let currentSum = arr[i] + arr[left] + arr[right];
      let diff = Math.abs(currentSum - target);

      if (diff < sum) {
        sum = diff;
        result = currentSum
      }

      if (currentSum == target) {
        return target
      }

      if (currentSum < target) {
        left++;
      } else {
        right--;
      }
    }
  }
  return result;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1)); // 2  
console.log(threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)) // -2
console.log(threeSumClosest([0, 0, 0], 1)); // 0
