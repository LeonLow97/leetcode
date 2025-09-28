// Write a function called same, which accepts two arrays. 
// The function should return true if every value in the array has it's 
// corresponding value squared in the second array. 
// The frequency of values must be the same.

// same([1,2,3], [4,1,9]) // true
// same([1,2,3], [1,9]) // false
// same([1,2,1], [4,4,1]) // false (must be same frequency)

// O(N^2)
// indexOf() is another loop
// The indexOf() method returns the first index at which a given 
// element can be found in the array, or -1 if it is not present.
// splice(start, deleteCount, item1, item2, itemN)
function same(arr1, arr2) {
    if (arr1.length != arr2.length) {
        return false
    }
    for (let i = 0; i < arr1.length; i++) {
        let correctIndex = arr2.indexOf(arr1[i] ** 2)
        if (correctIndex === -1) {
            return false;
        }
        console.log("arr2", arr2)
        arr2.splice(correctIndex, 1)
    }
    return true
}

console.log(same([1,2,3,2], [9,1,4,4]))

// Refactored - O(N)
// 2 loops but not nested
// Using an object to compile the values
function sameRefactored(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false
    }
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    // Storing the keys and counting how many times this value occurs
    for (let val of arr1) {
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }
    for (let val of arr2) {
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1
    }
    for (let key in frequencyCounter1) {
        // Checking if keys are similar
        if (!(key ** 2 in frequencyCounter2)) {
            return false
        }
        // Checking if values are similar
        if (frequencyCounter2[key ** 2] !== frequencyCounter1[key]) {
            return false
        }
    }
    console.log(frequencyCounter1)
    console.log(frequencyCounter2)
    return true
}

console.log(sameRefactored([1,2,3,2], [9,1,4,4]))
console.log("\n")
console.log(sameRefactored([1,2,3,2,5], [9,1,4,4,11]))