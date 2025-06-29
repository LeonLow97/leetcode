// Merging Arrays Pseudocode
// Create an empty array, take a look at the smallest values in each input array.

// If the value in the first array is smaller than the value in the second array,
// push the value in the first array into the results and move on to the next value in the first array.

// If the value in the first array is larger than the value in the second array,
// push the value in the second array into the results and move on to the next value in the second array.

// Once we exhaust one array (arrays may be of different size), push in all remaining
// values from the other array

// my solution
function mergeArrays(arr1, arr2) {
  let results = [];

  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      results.push(arr1[i]);
      i++;
    } else if (arr2[j] < arr1[i]) {
      results.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    results.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    results.push(arr2[j]);
    j++;
  }

  return results;
}

console.log(mergeArrays([1, 10, 50], [2, 14, 99, 100]));
console.log(mergeArrays([], [1, 3]));
console.log(mergeArrays([100], [1, 2, 3, 4, 20]));
