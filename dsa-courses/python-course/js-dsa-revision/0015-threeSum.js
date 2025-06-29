/*
Difficulty: MEDIUM
No.15    https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
*/

var threeSum = function (arr) {
  // base case
  if (arr.length === 3) {
    let sum = arr[0] + arr[1] + arr[2];
    return sum === 0 ? [arr] : [];
  }

  // sort the array
  arr.sort(function (a, b) {
    return a - b;
  });
  console.log(arr);

  // define pointers
  let result = [];

  // iterate through array
  for (let i = 0; i < arr.length; i++) {
    if (i !== 0 && arr[i] === arr[i - 1]) continue;

    let left = i + 1;
    let right = arr.length - 1;
    while (left < right) {
      let sum = arr[i] + arr[left] + arr[right];
      if (sum === 0) {
        result.push([arr[i], arr[left], arr[right]]);
        left++;
        right--;

        while (left < right && arr[left] === arr[left - 1]) {
          left++;
        }

        while (left < right && arr[right] === arr[right + 1]) {
          right--;
        }
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  // return result array
  return result;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4])); // [[-1,-1,2],[-1,0,1]]
console.log(threeSum([0, 1, 1])); // []
console.log(threeSum([0, 0, 0])); // [0,0,0]
