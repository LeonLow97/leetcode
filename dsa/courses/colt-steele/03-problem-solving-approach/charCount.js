// Write a function which takes in a string
// and returns counts of each character in the string

function charCount(str) {
    // Convert all uppercase to lowercase
    let string = str.toLowerCase()
    let result = {}
    for (char of string) {
        // use RegExp to check for numbers and alphabets in a string (to remove any whitespaces or special characters)
        let pattern = /[a-z0-9]/
        if (pattern.test(char)) {
            // if character already exists, we add 1 to it
            if (result[char] > 0) {
                result[char]++
            // if character does not exist, we initialize it with 1
            } else {
                result[char] = 1
            }
        }
    }

    // return object with counts of each character
    return result
}

console.log(charCount("Hello Jie Wei"))
console.log(charCount("Good morning, nice to meet you!"))