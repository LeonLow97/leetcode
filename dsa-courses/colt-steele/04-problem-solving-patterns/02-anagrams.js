// Given 2 strings, write a function to determine if the second string is an anagram of the first.
// An anagram is a word, phrase, or name formed by rearranging the letters of another,
// such as cinema formed form iceman. 

// validAnagram('', '') // true
// validAnagram('aaz', 'zza') // false
// validAnagram('anagram', 'nagaram') // true
// validAnagram("rat","car") // false) // false
// validAnagram('awesome', 'awesom') // false
// validAnagram('qwerty', 'qeywrt') // true
// validAnagram('texttwisttime', 'timetwisttext') // true

// My Solution
function validAnagram(str1, str2) {
    if (str1.length !== str2.length) {
        return false
    }
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    for (let val of str1) {
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }
    for (let val of str2) {
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

console.log(validAnagram('','')) // true
console.log(validAnagram('aaz', 'zza')) // false
console.log(validAnagram('anagram', 'nagaram')) // true
console.log(validAnagram("rat","car")) // false
console.log(validAnagram('awesome', 'awesom')) // false
console.log(validAnagram('qwerty', 'qeywrt')) // true
console.log(validAnagram('texttwisttime', 'timetwisttext')) // true

// Teacher's Solution
function validAnagram2(first, second) {
    if (first.length !== second.length) {
        return false
    }
    
    const lookup = {}

    for (let i = 0; i < first.length; i++) {
        let letter = first[i]
        // if letter exists, increment, otherwise set to 1.
        lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1
    }

    for (let i = 0; i < second.length; i++) {
        let letter = second[i]
        if (!lookup[letter]) {
            return false
        } else {
            lookup[letter] -= 1
        }
    }
    return true
}

console.log("Teacher's Solution")
console.log(validAnagram2('','')) // true
console.log(validAnagram2('aaz', 'zza')) // false
console.log(validAnagram2('anagram', 'nagaram')) // true
console.log(validAnagram2("rat","car")) // false
console.log(validAnagram2('awesome', 'awesom')) // false
console.log(validAnagram2('qwerty', 'qeywrt')) // true
console.log(validAnagram2('texttwisttime', 'timetwisttext')) // true