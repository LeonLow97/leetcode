// Write a function called isSubsequence which takes in two strings and checks whether the 
// characters in the first string form a subsequence of the characters in the second string. 
// In other words, the function should check whether the characters in the first string appear 
// somewhere in the second string, without their order changing.

/* Your solution MUST have AT LEAST the following complexities:
Time Complexity - O(N + M))
Space Complexity - O(1) */

// isSubsequence('hello', 'hello world'); // true
// isSubsequence('sing', 'sting'); // true
// isSubsequence('abc', 'abracadabra'); // true
// isSubsequence('abc', 'acb'); // false (order matters)

function isSubsequence(str1, str2) {
    let index1 = 0
    let index2 = 0
    if (str1.length === 0) {
        return true
    }
    while (index2 < str2.length) {
        if (str1[index1] === str2[index2]) {
            index1++
        }
        if (index1 === str1.length) {
            return true
        }
        index2++
    }
    return false
}

console.log(isSubsequence('hello', 'hello world')); // true
console.log(isSubsequence('sing', 'sting')); // true
console.log(isSubsequence('abc', 'abracadabra')); // true
console.log(isSubsequence('abc', 'acb')) // false