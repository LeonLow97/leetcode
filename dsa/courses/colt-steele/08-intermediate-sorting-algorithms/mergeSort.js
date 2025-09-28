// Merge Sort PseudoCode
// Break up the array into halves (slice) until you have arrays
// that are empty or have 1 element (arr.length <= 1)
// Once you have smaller sorted arrays, merge those arrays with
// other sorted arrays until you are back at the full length of the array.
// Once the array has been merged together, return the merged (and sorted) array.

function mergeArray(arr1, arr2) {
  let result = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else if (arr2[j] < arr1[i]) {
      result.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  let mid = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, mid));
  let right = mergeSort(arr.slice(mid));   // waits for the recursion of 'left' above until it returns something.
  return mergeArray(left, right);
}

console.log(mergeSort([2, 5, 31, 6, 89, 43, 13]));
console.log(mergeSort([10, 24, 76, 73]));

