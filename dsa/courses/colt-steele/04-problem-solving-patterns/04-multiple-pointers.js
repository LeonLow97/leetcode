// Implement a function called countUniqueValues,
// which accepts a sorted array, and counts the unique values in the array.
// There can be negative numbers in the array, but it will always be sorted.

// countUniqueValues([1,1,1,1,1,2]) // 2
// countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]) // 7
// countUniqueValues([]) // 0
// countUniqueValues([-2,-1,-1,0,1]) // 4

// My Solution
// Time Complexity - O(N)
function countUniqueValues(arr) {
    let left = 0;
    let right = 1;
    if (arr.length === 0) {
        return 0
    }
    while (left < right) {
        // compare both values
        if (arr[left] === arr[right]) {
            right += 1
        } else if (arr[left] !== arr[right]) {
            left += 1
            arr[left] = arr[right]
            right += 1
        }
        if (right === arr.length) {
            return left + 1
        }
    }
}

console.log(countUniqueValues([1,1,1,1,1,1,2]))
console.log(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]))
console.log(countUniqueValues([]))
console.log(countUniqueValues([-2,-1,-1,0,1]))

// Teacher's Solution
function countUniqueValuesSolution(arr) {
    if (arr.length == 0) return 0;
    var i = 0;
    for (var j = 1; j < arr.length; j++) {
        if (arr[i] !==  arr[j]) {
            i++;
            arr[i] = arr[j]
        }
    }
    return i + 1
}

console.log(`Teacher's Solution`)
console.log(countUniqueValuesSolution([1,1,1,1,1,1,2]))
console.log(countUniqueValuesSolution([1,2,3,4,4,4,7,7,12,12,13]))
console.log(countUniqueValuesSolution([]))
console.log(countUniqueValuesSolution([-2,-1,-1,0,1]))