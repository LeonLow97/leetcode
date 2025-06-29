// Write a function called sameFrequency Given two positive integers, 
// find out if the two numbers have the same frequency of digits.
// Your solution MUST have the following complexities: Time: O(N)

// sameFrequency(182,281) // true
// sameFrequency(34,14) // false
// sameFrequency(3589578, 5879385) // true
// sameFrequency(22,222) // false

function sameFrequency(num1, num2) {
    // Ensure both numbers have the same length
    if (num1.toString().length !== num2.toString().length) {
        return false
    }

    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    // Storing key-value pairs of both numbers
    for (let val of num1.toString()) {
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }
    for (let val of num2.toString()) {
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1
    }
    for (let key in frequencyCounter1) {
        if (!(key in frequencyCounter2)) {
            return false
        }
        if (frequencyCounter1[key] !== frequencyCounter2[key]) {
            return false
        }
    }
    return true
}

console.log(sameFrequency(182,281)) // true
console.log(sameFrequency(34,14)) // false
console.log(sameFrequency(3589578, 5879385)) // true
console.log(sameFrequency(22,222)) // false