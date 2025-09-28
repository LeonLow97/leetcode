// Naive String Search Pseudocode
// Loop over the longer string
// Loop over the shorter string
// If the characters don't match, break out of the inner loop
// If the characters do match, keep going.
// If you complete the inner loop and find a match, increment the count of matches.
// Return the count

function naiveStringSearch(str, substr) {
  let count = 0;

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < substr.length; j++) {
            if (substr[j] !== str[i + j]) {
                break
            }
            if (j === substr.length - 1) {
                count++
            }
        }
    }

  return count;
}

console.log(naiveStringSearch("iajsfhaoapfdhpaaopasjf", "ha")); // 1
console.log(naiveStringSearch("woozomgsooowomgmg", "omg")) // 2
console.log(naiveStringSearch("oojgeoofaefofooodmoof", "oo")) // 5
