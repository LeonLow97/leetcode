// Bubble Sort Pseudocode
// Start looping from with a variable called i at the end of the array towards the beginning
// Start an inner loop with a variable called j from the beginning until i - 1
// If arr[j] is greater than arr[j + 1], swap those 2 values
// return the sorted array

// ES5 Swapping
function bubbleSort(arr) {
  var noSwaps;
  for (let i = arr.length; i > 0; i--) {
    noSwaps = true;
    for (let j = 0; j < i - 1; j++) {  // compare first value with the rest of i - 1 values
      console.log(arr, arr[j], arr[j+1])
      if (arr[j] > arr[j + 1]) {
        var temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        noSwaps = false;
      }
    }
    // optimization
    console.log("[i]:",i)
    if (noSwaps) break;
  }
  return arr;
}

// console.log(bubbleSort([37, 45, 29, 8, 105, -3]));
console.log(bubbleSort([8,1,2,3,4,5,6,7]))

// // ES2015 Swapping
// function bubbleSort(arr) {
//   for (let i = arr.length; i > 0; i--) {
//     for (let j = 0; j < i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
//       }
//     }
//   }
//   return arr;
// }

// console.log(bubbleSort([37, 45, 29, 8, 105, -3]));

// naive approach (not optimized)
// Every loop reaches the end of the bubble sort even though
// the last few elements were already sorted to the largest
// as the larger values bubble to the top at the beginning of the sorting process.
// function bubbleSort(arr) {
//   for (var i = 0; i < arr.length; i++) {
//     for (var j = 0; j < arr.length; j++) {
//       if (arr[j] > arr[j + 1]) {
//         var temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
//   return arr;
// }

// console.log(bubbleSort([37, 45, 29, 8]))
