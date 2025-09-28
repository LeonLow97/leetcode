/*
Difficulty: MEDIUM
No.11    https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 10^4
*/

// My Solution
var maxArea = function (arr) {
  // base case
  if (arr.length == 2) return Math.min(arr[0], arr[1]);

  // define pointers
  let left = 0;
  let right = arr.length - 1;
  let lowerSide, currentArea;
  let highestArea = 0;
  let width = arr.length - 1;

  while (width > 0) {
    lowerSide = Math.min(arr[left], arr[right]);
    currentArea = lowerSide * width;
    if (currentArea > highestArea) {
      highestArea = currentArea;
    }
    if (arr[left] < arr[right]) {
      left++;
    } else if (arr[right] < arr[left]) {
      right--;
    } else {
        right--
    }
    width--;
  }
  return highestArea;
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])); // 49 (8 iterations)
console.log(maxArea([1, 3, 2, 5, 25, 24, 5])); // 24 (6 iterations)
console.log(maxArea([1, 1])); // 1 (1 iteration)
console.log(maxArea([1, 2])); // 2

// Tutor's Solution
var maxAreaSolution = function(arr) {
    // define pointers, max area
    let left = 0
    let right = arr.length - 1;
    let maxArea = 0;

    // find max area
    while (left < right) {
        // (right - left) is the width
        let area = (right - left) * Math.min(arr[left], arr[right]);
        maxArea = Math.max(maxArea, area);
        if (arr[left] < arr[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea
}

console.log("Tutor's Solution......")
console.log(maxAreaSolution([1, 8, 6, 2, 5, 4, 8, 3, 7])); // 49 (8 iterations)
console.log(maxAreaSolution([1, 3, 2, 5, 25, 24, 5])); // 24 (6 iterations)
console.log(maxAreaSolution([1, 1])); // 1 (1 iteration)
console.log(maxAreaSolution([1, 2])); // 2

