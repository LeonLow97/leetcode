/*
Difficulty: HARD
No.42    https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
*/

// Don't know how to do this question (need to practice this!)
// Tutor's Solution
var trap = function(arr) {
    // base case
    if (arr.length < 3) return 0;

    // find index position with highest elevation
    let max = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > arr[max]) {
            max = i
        }
    }
    
    let sum = 0;

    // define pointers and iterate till max elevation
    let leftMax = 0;
    for (let i = 0; i < max; i++) {
        if (arr[i] > arr[leftMax]) {
            leftMax = i;
        }
        sum += arr[leftMax] - arr[i]
    }

    let rightMax = arr.length - 1;
    for (let i = arr.length - 1; i > max; i--) {
        if (arr[i] > arr[rightMax]) {
            rightMax = i
        }
        sum += arr[rightMax] - arr[i]
    }
    return sum
} 

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1])) // 6
console.log(trap([4,2,0,3,2,5])) // 9