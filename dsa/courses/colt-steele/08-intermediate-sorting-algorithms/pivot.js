//Pivot Pseudocode
// It will help to accept 3 arguments: an array, a start index, and an end index
// (these can default to 0 and the array length minus 1, respectively)
// Grab the pivot from the start of the array
// Store the current pivot index in a variable (this will keep track of where the pivot should end up)
// Loop through the array from the start until the end.
// If the pivot is greater than the current element, increment the pivot index variable
// and then swap the current element with the element at the pivot index.
// Swap the starting element (i.e., the pivot) with the pivot index.

function swap(arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

// my solution
function pivot(arr, start = 0, end = arr.length - 1) {
  let pivot = arr[start];
  let pivotIndex = start;

  for (let i = start + 1; i < arr.length; i++) {
    if (pivot > arr[i]) {
      pivotIndex++;
      swap(arr, i, pivotIndex);
    }
  }
  swap(arr, start, pivotIndex);
  return pivotIndex;
}

console.log(pivot([5, 2, 1, 8, 4, 7, 6, 3]));
console.log(pivot([4, 8, 2, 1, 5, 7, 6, 3]));
