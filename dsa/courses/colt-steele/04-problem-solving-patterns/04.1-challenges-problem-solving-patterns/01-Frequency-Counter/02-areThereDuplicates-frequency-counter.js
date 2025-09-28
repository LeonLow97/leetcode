// Implement a function called, areThereDuplicates which accepts a variable number of arguments, 
// and checks whether there are any duplicates among the arguments passed in.  You can solve this 
// using the frequency counter pattern OR the multiple pointers pattern.
/* Restrictions:
Time - O(n)
Space - O(n)
Bonus:
Time - O(n log n)
Space - O(1) */

// areThereDuplicates(1, 2, 3) // false
// areThereDuplicates(1, 2, 2) // true 
// areThereDuplicates('a', 'b', 'c', 'a') // true 

function areThereDuplicatesFC(...args) {
    let frequencyCounter = {}
    for (let val of args) {
        frequencyCounter[val] ? frequencyCounter[val] += 1 : frequencyCounter[val] = 1
    }
    for (let key in frequencyCounter) {
        if (frequencyCounter[key] > 1) {
            return true
        }
    }
    return false
}

console.log("Using Frequency Counter")
console.log(areThereDuplicatesFC(1, 2, 3)) // false
console.log(areThereDuplicatesFC(1, 2, 2)) // true 
console.log(areThereDuplicatesFC('a', 'b', 'c', 'a')) // true 

function areThereDuplicatesMP(...args) {
    args.sort();
    console.log(args)
    let left = 0
    let right = 1
    while (right < args.length) {
        if (args[left] === args[right]) {
            return true
        } 
        left++
        right++
    }
    return false
}

console.log("Using Multiple Pointers")
console.log(areThereDuplicatesMP(1, 2, 3)) // false
console.log(areThereDuplicatesMP(1, 2, 2)) // true 
console.log(areThereDuplicatesMP('a', 'b', 'c', 'a')) // true