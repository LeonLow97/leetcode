// Selection Sort Pseudocode
// Store the first element as the smallest value you've seen so far.
// Compare this item to the next item in the array until you find a smaller number.
// If a smaller number is found, designate that smaller number to be the new "minimum" and continue until the end of the array.
// If the "minimum" is not the value (index) you initially began with, swap the 2 values.
// Repeat this with the next element until the array is sorted.

function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let lowest = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[lowest]) {
        lowest = j; // updated the value of lowest using the index
      }
    }
    // swap 
    if (i !== lowest) { // if i and lowest is the same, we don't swap (reduce iterations)
      var temp = arr[i];
      arr[i] = arr[lowest];
      arr[lowest] = temp;
    }
  }
  return arr;
}

console.log(selectionSort([0, 2, 34, 22, 10, 19, 17]));

/*
i,j,lowest
0,1,1
0,2,2
0,3,2
0,4,2
*/

// SWAP ES2015
// function selectionSortES2015(arr) {
//   const swap = (arr, idx1, idx2) =>
//     ([arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]);

//   for (let i = 0; i < arr.length; i++) {
//     let lowest = i;
//     for (let j = i + 1; j < arr.length; j++) {
//       if (arr[j] < arr[lowest]) {
//         lowest = j; // updated the value of lowest using the index
//       }
//     }
//     // swap
//     if (i !== lowest) swap(arr, i, lowest);
//   }
//   return arr;
// }

// console.log(
//   "USING ES2015 SWAP",
//   selectionSortES2015([0, 2, 34, 22, 10, 19, 17])
// );
