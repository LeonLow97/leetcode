// Write a recursive function called capitalizeFirst.
// Given an array of strings, capitalize the first letter of each string in the array.

function capitalizeFirst(arr) {
  let result = [];

  if (arr.length === 0) {
    return []
  }

  result.push(arr[0][0].toUpperCase() + arr[0].slice(1));

  result = result.concat(capitalizeFirst(arr.slice(1)));

  return result;
}

console.log(capitalizeFirst(["car", "taco", "banana"])); // ['Car','Taco','Banana']
