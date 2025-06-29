/*
Difficulty: EASY
No.977    https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of 
the squares of each number sorted in non-decreasing order.

Constraints:

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.
*/

// My Solution (~1100ms) BAD
var swap = function(arr, idx1, idx2) {
    var temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp;
}

var sortedSquares = function(arr) {
    // base cases
    if (arr.length < 1) return [];
    if (arr.length === 1) return [arr[0] ** 2]

    // define pointers
    let L = 0;
    let R = 1;

    for (let i = 0; i < arr.length; i++) {
        arr[i] = Math.pow(arr[i], 2)
    }

    while (L < arr.length) {
        if (arr[R] < arr[L]) {
            swap(arr, L, R)
        }
        if (R === arr.length - 1) {
            L++;
            R = L
            continue
        }
        R++
    }
    return arr
}

console.log("My Solution:")
console.log(sortedSquares([-4,-1, 0,3,10])) // [0,1,9,16,100] 19 iterations
console.log(sortedSquares([-7,-3,2,3,11])) // [4,9,9,49,121] 19 iterations
console.log(sortedSquares([-5, -3, -2, -1])) // [1,4,9,25] 13 iterations

// Tutor's Solution 1 (~190ms)
// The greatest value will either be on the leftmost or rightmost of the array
function sortedSquares1(arr) {
    if (arr.length === 1) return [arr[0] ** 2]
    let countIterations = 0

    let L = 0;
    let R = arr.length - 1
    let index = arr.length - 1;

    let result = [];

    while (index >= 0) {
        let leftSquared = arr[L] ** 2;
        let rightSquared = arr[R] ** 2;
        if (rightSquared > leftSquared) {
            result[index] = rightSquared;
            index--
            R--;
        } else {
            result[index] = leftSquared;
            index--
            L++
        }
    }
    return result
}

console.log("\nTutor Solution 1:")
console.log(sortedSquares1([-4,-1, 0,3,10])) // [0,1,9,16,100] 5 iterations
console.log(sortedSquares1([-7,-3,2,3,11])) // [4,9,9,49,121] 5 iterations
console.log(sortedSquares1([-5, -3, -2, -1])) // [1,4,9,25] 4 iterations

// Tutor's Solution 2
// find the smallest value indexed and start from there
function sortedSquares2(arr) {
    let smallestIdx = 0;
    for (let i = 0; i < arr.length; i++) {
        smallestIdx = i;
        if (arr[i] >= 0) break;
    }

    // define pointers (start from the smallest value in the array)
    let L = smallestIdx - 1;
    let R = smallestIdx;
    let result = [];
    let index = 0;

    while (L >= 0 && R <= arr.length - 1) {
        let leftSquared = arr[L] ** 2;
        let rightSquared = arr[R] ** 2
        if (rightSquared < leftSquared) {
            result[index] = rightSquared;
            R++;
        } else {
            result[index] = leftSquared
            L--;
        }
        index++;
    }

    while (R <= arr.length - 1) {
        result[index] = arr[R] ** 2
        index++
        R++
    }

    while (L >= 0) {
        result[index] = arr[L] ** 2
        index++
        L--
    }
    return result
}

console.log("\nTutor Solution 2:")
console.log(sortedSquares2([-4,-1, 0,3,10])) // [0,1,9,16,100] 8 Iterations
console.log(sortedSquares2([-7,-3,2,3,11])) // [4,9,9,49,121] 8 Iterations
console.log(sortedSquares2([-5, -3, -2, -1])) // [1,4,9,25]  8 Itera tions


