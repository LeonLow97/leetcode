// Quick Sort PseudoCode
// Call the pivot helper on the array.
// When the helper returns to you the updated pivot index, recursively
// call the pivot helper on the subarray to the left of that index, and the
// subarray to the right of that index.
//

function swap(arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

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

function quickSort(arr, left = 0, right = arr.length - 1) {
  // base case
  if (left < right) {
    let pivotIndex = pivot(arr, left, right);
    // left (recursive)
    quickSort(arr, left, pivotIndex - 1);
    // right (recursive)
    quickSort(arr, pivotIndex + 1, right);
  }

  return arr;
}

console.log(quickSort([5, 2, 1, 8, 4, 7, 6, 3]));
console.log(quickSort([4, 8, 2, 1, 5, 7, 6, 3]));
console.log(quickSort([4, 8, 2123, 1, 325, 7, 126, -3]));
