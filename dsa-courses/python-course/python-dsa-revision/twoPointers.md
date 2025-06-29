# Two Pointers

- Check if the array is sorted or unsorted.

## isSubsequence

```js
// Write a function called isSubsequence which takes in two strings and checks whether the
// characters in the first string form a subsequence of the characters in the second string.
// In other words, the function should check whether the characters in the first string appear
// somewhere in the second string, without their order changing.

/* Your solution MUST have AT LEAST the following complexities:
Time Complexity - O(N + M))
Space Complexity - O(1) */

function isSubsequence(str1, str2) {
  let index1 = 0;
  let index2 = 0;
  if (str1.length === 0) {
    return true;
  }
  while (index2 < str2.length) {
    if (str1[index1] === str2[index2]) {
      index1++;
    }
    if (index1 === str1.length) {
      return true;
    }
    index2++;
  }
  return false;
}

console.log(isSubsequence("hello", "hello world")); // true
console.log(isSubsequence("sing", "sting")); // true
console.log(isSubsequence("abc", "abracadabra")); // true
console.log(isSubsequence("abc", "acb")); // false
```

## averagePair

```js
// Write a function called averagePair. Given a sorted array of integers and a target average,
// determine if there is a pair of values in the array where the average of the pair equals the target average.
// There may be more than one pair that matches the average target.
/* Bonus Constraints:
Time: O(N)
Space: O(1) */

function averagePair(arr, avg) {
  if (arr.length === 0) {
    return false;
  }
  let left = 0;
  let right = 1;
  while (right < arr.length) {
    let average = (arr[left] + arr[right]) / 2;
    console.log(average);
    if (average === avg) {
      return true;
    } else if (average !== avg) {
      right++;
      if (right === arr.length) {
        left++;
        right = left + 1;
      }
    }
  }
  return false;
}

console.log(averagePair([1, 2, 3], 2.5)); // true
// console.log(averagePair([1,3,3,5,6,7,10,12,19],8)) // true
// console.log(averagePair([-1,0,3,4,5,6], 4.1)) // false
// console.log(averagePair([],4)) // false
```

## countUniqueValues

```js
function countUniqueValues(arr) {
  if (arr.length == 0) return 0;
  var i = 0;
  for (var j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1;
}

console.log(`Teacher's Solution`);
console.log(countUniqueValues([1, 1, 1, 1, 1, 1, 2]));
console.log(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]));
console.log(countUniqueValues([]));
console.log(countUniqueValues([-2, -1, -1, 0, 1]));
```

## sumZero

```js
// Write a function called sumZero which accepts a sorted array of integers.
// The function should find the first pair where the sum is 0. Return an array
// that includes both values that sum to zero or undefined if a pair does not exist

// Time Complexity - O(N)
// Space Complexity - O(1)
function sumZero(arr) {
  let left = 0;
  let right = arr.length - 1;
  // don't want to put left <= right in case the number is zero.
  while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}

console.log(sumZero([-4, -3, -2, -1, 0, 1, 2, 5]));
```
