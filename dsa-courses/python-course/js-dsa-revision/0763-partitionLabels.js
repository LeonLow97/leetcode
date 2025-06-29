/*
Difficulty: MEDIUM
No.763    https://leetcode.com/problems/partition-labels/

You are given a string s. We want to partition the string into as 
many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the 
parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:

- 1 <= s.length <= 500
- s consists of lowercase English letters.
*/

var partitionLabels = function(str) {
    let arr = str.split("");
    let frequencyCounter = []

    // find the last index each character appears in the string
    for (let i = 0; i < arr.length; i++) {
        frequencyCounter[arr[i]] = i;
    }

    let left = 0;
    let right = 0;
    let index = 0;
    let result = [];

    while (index < arr.length) {
        let currentChar = arr[index];
        right = Math.max(right, frequencyCounter[currentChar])
        if (right === index) {
            result.push(right - left + 1);
            right++;
            left = right;
        }
        index++;
    }

    return result;
}

console.log(partitionLabels("ababcbacadefegdehijhklij")) // [9,7,8]
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
console.log(partitionLabels("eccbbbbdec")) // [10]