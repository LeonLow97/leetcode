// Given a sorted array of integers, write a function called search, 
// that accepts a value and returns the index where the value passed 
// to the function is located. If the value is not found, return -1

// search([1,2,3,4,5,6],4) // 3
// search([1,2,3,4,5,6],6) // 5
// search([1,2,3,4,5,6],11) // -1

// Naive Solution
// Time Complexity - O(N)
function search(arr, num) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === num) {
            return i
        }
    }
    return -1;
}

console.log(search([1,2,3,5,6,10], 6))

// Refactor
// Time Complexity - Log(N) - Binary Search
function searchRefactor(arr, num) {
    let min = 0
    let max = arr.length - 1

    while (min <= max) {
        let middle = Math.floor((min + max)/2)
        let middleNumber = arr[middle]

        if (middleNumber < num) {
            min = middle + 1
        } else if (middleNumber > num) {
            max = middle + 1
        } else {
            return middle
        }
    }
    return -1
}

console.log(search([1,2,3,5,6,10], 6))
