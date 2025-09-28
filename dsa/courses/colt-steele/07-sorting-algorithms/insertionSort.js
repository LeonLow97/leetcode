// Insertion Sort Pseudocode
// Start by picking the second element in the array
// Now compare the second element with the one before it and swap if necessary
// Continue to the next element and if it is in the incorrect order, iterate though the sorted
// portion (i.e., left side) to place the element in the correct place.
// Repeat until the array is sorted.

function insertionSort(arr) {
  for (var i = 1; i < arr.length; i++) {
    // 'right'
    let currentVal = arr[i];
    let index = i;
    for (let j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
      // 'left'
      arr[j + 1] = arr[j]; // [2,1,9,76,76] on the last loop with value '4'
      index = j;
    }
    // insert currentVal into the arr
    // can access it outside that for loop because we use 'var'
    console.log(index);
    arr[index] = currentVal;
  }
  return arr;
}

console.log(insertionSort([1, 2, 9, 76, 4]));
