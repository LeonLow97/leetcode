/*
Given a sorted array and a number, write a function called sortedFrequency that counts the occurrences of the number in the array

sortedFrequency([1,1,2,2,2,2,3],2) // 4 
sortedFrequency([1,1,2,2,2,2,3],3) // 1 
sortedFrequency([1,1,2,2,2,2,3],1) // 2 
sortedFrequency([1,1,2,2,2,2,3],4) // -1
Time Complexity - O(log n)
*/

// My Solution
function sortedFrequency(arr, num) {
    let left = 0
    let right = arr.length
    let count = 0

    while (left < right) {
        let middle = Math.floor((left + right) / 2)

        if (num < arr[middle]) right = middle
        if (num > arr[middle]) left = middle

        if (arr[right] === num) count++
        if (arr[left] === num) count++
        
        right--
        left++
    }

    return count === 0 ? -1 : count
}

console.log(sortedFrequency([1,1,2,2,2,2,3],2)) // 4 
console.log(sortedFrequency([1,1,2,2,2,2,3],3)) // 1 
console.log(sortedFrequency([1,1,2,2,2,2,3],1)) // 2 
console.log(sortedFrequency([1,1,2,2,2,2,3],4)) // -1