// Write a recursive function called flatten which accepts
// an array of arrays and returns a new array with all values flattened.

function flatten(arr) {
  let result = [];

  for (let element of arr) {
    // check if element is an array
    if (element.length > 0) {
      result = result.concat(flatten(element));
    } else {
      result.push(element);
    }
  }
  return result;
}

console.log(flatten([1, 2, 3, [4, 5]])); // [1, 2, 3, 4, 5]
console.log(flatten([1, [2, [3, 4], [[5]]]])); // [1, 2, 3, 4, 5]
console.log(flatten([[1], [2], [3]])); // [1,2,3]
console.log(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])); // [1,2,3]
