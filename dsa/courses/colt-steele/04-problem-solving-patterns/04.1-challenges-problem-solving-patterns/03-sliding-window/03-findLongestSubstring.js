// Write a function called findLongestSubstring, which accepts
// a string and returns the length of the longest substring with all 
// distinct characters

// Time Complexity - O(N)

function findLongestSubstring(str) {
    let length = 0;
    let start = 0;
    let store = {}

    for (let i = 0; i < str.length; i++) {
        let char = str[i]
        // if the char repeats, change the start position to that character
        if (store[char]) {
            start = Math.max(start, store[char])
        }
        // find the length of non-repeats (take end - start)
        length = Math.max(length, i - start + 1) 
        store[char] = i + 1
        
    }
    return length
}

console.log(findLongestSubstring('')) // 0
console.log(findLongestSubstring('rithmschool')) // 7
console.log(findLongestSubstring('thisisawesome')) // 6
console.log(findLongestSubstring('thecatinthehat')) // 7
console.log(findLongestSubstring('bbbbbb')) // 1
console.log(findLongestSubstring('longestsubstring')) // 8
console.log(findLongestSubstring('thisishowwedoit')) // 6