/*
Given an array of 1s and 0s which has all 1s first followed by all 0s, 
write a function called countZeroes, which returns the number of zeroes in the array.

countZeroes([1,1,1,1,0,0]) // 2
countZeroes([1,0,0,0,0]) // 4
countZeroes([0,0,0]) // 3
countZeroes([1,1,1,1]) // 0
Time Complexity - O(log n)
*/

// My Solution (Considered all cases which not ideal, see refactored below)
function countZeroes(arr) {
  let left = 0;
  let right = arr.length - 1;
  let count = 0;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);

    // 111
    if (arr[middle] === 1 && arr[middle + 1] === 1) {
      left = middle + 2;
      // 110
    } else if (arr[middle] === 1 && arr[middle + 1] === 0) {
      let result = arr.slice(middle + 1);
      count += result.length;
      break;
      // 100
    } else if (arr[middle] === 0 && arr[middle - 1] === 1) {
      let result = arr.slice(middle);
      count += result.length;
      break;
      // 000
    } else if (arr[middle] === 0 && arr[middle - 1] === 0) {
      right = middle - 2;
      if (right < 0) {
        return arr.length;
      }
    } else {
      break;
    }
  }
  return count;
}

console.log(countZeroes([1, 1, 1, 1, 0, 0])); // 2
console.log(countZeroes([1, 0, 0, 0, 0])); // 4
console.log(countZeroes([0, 0, 0])); // 3
console.log(countZeroes([1, 1, 1, 1])); // 0

// Refactored Solution
function countZeroes_refactored(arr) {
    let left = 0
    let right = arr.length

    while (left < right) {
        let middle = Math.floor((left + right) / 2)

        if (arr[middle] === 1) {
            left = middle + 1
        } else if (arr[middle] === 0) {
            right = middle - 1
        } else {
            return null
        }
    }
    return arr.length - left
}

console.log("countZeroes Refactored.....")
console.log(countZeroes_refactored([1, 1, 1, 1, 0, 0])); // 2
console.log(countZeroes_refactored([1, 0, 0, 0, 0])); // 4
console.log(countZeroes_refactored([0, 0, 0])); // 3
console.log(countZeroes_refactored([1, 1, 1, 1])); // 0
