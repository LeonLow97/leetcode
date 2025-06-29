# Intermediate Sorting Algorithms

## Objectives

- Understand the limitations of the basic sorting algorithms (selection, bubble, and insertion sort)
- Implement merge sort
- Implement quick sort
- Implement radix sort

## Faster Sorts

- There is a family of sorting algorithms that can improve time complexity from O(N^2) to O(N log N).
- There's a tradeoff between efficiency and simplicity.
- The more efficient algorithms are less simple, and generally take longer to understand.

## Merge Sort

- [Intermediate Sort Slides](https://cs.slides.com/colt_steele/intermediate-sorting-algorithms)
- Combination of 2 things - merging and sorting
- Exploits the fact that arrays of 0 or 1 element are always sorted.
- Works by decomposing an array into smaller arrays of 0 or 1 elements, then building up a newly sorted array.
- Solved through recursion

```js
/*
                    [8, 3, 5, 4, 7, 6 , 1, 2]
                [8, 3, 5 ,4]              [7, 6, 1, 2]    
        [8, 3]      [5, 4]           [7, 6]      [1, 2]
    [8]    [3]    [5]    [4]       [7]    [6]    [1]    [2] 
        [3, 8]        [4, 5]          [6, 7]         [1, 2]     // sorting starts here (starts with smaller size arrays)
            [3, 4, 5, 8]                 [1, 2, 6, 7]
                    [1, 2, 3, 4, 5, 6, 7, 8]

*/
```

### Merging Arrays (First step for Merge Sort)

- Merging 2 _sorted_ arrays
- In order to implement merge sort, it's useful to first implement a function responsible for merging 2 sorted arrays.
- Given 2 arrays which are sorted, this helper function should create a new array which is also sorted, and consists of all of the elements in the 2 input arrays.
- This function should run in **O(n + m)** time and **O(n + m)** space and should not modify the parameters passed to it.

---

### Merging Arrays PseudoCode

```js
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  let mid = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, mid));
  let right = mergeSort(arr.slice(mid)); // waits for the recursion of 'left' above until it returns something.
  return mergeArray(left, right);
}
```

---

### Big O of mergeSort

| Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| :--------------------: | :-----------------------: | :---------------------: | :--------------: |
|       O(n log n)       |        O(n log n)         |       O(n log n)        |       O(n)       |

- O(log n) decompositions
  - making splits until arr.length <= 1
- O(n) comparisons per decomposition
  - comparing 2 arrays, it will be the size of the original array.

---

## Quick Sort

- Like merge sort, exploits the fact that arrays of 0 or 1 element are always sorted.
- Works by selecting 1 element (called the "pivot") and finding the index where the pivot should end up in the sorted array.
- Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot.

```js
/*
[5, 2, 1, 8, 4, 7, 6, 3]  // pick the first element '5'
[3, 2, 1, 4, 5, 7, 6, 8]  // only 5 is sorted now (in the correct position)
[1, 2, 3, 4, 5, 7, 6, 8]  // 3 is sorted now
[1, 2, 3, 4, 5, 6, 7, 8]
*/
```

---

### Pivot Helper

- In order to implement merge sort, it's useful to first implement a function responsible arranging elements in an array on either side of a pivot.
- Given an array, this helper function should designate an element as the pivot.
- It should then rearrange elements in the array so that all values less than the pivot are moved to the left of the pivot, and all values greater than the pivot are moved to the right of the pivot.
- The order of elements on either side of the pivot doesn't matter.
- The helper should do this **in place**, i.e., it should not create a new array.
- When complete, the helper should return the index of the pivot.

### Picking a Pivot

- The runtime of quick sort depends in part on how one selects the pivot.
- Ideally, the pivot should be chosen so that it's roughly the median value in the data set you're sorting.
- For simplicity, we will always choose the pivot to be the first element. (there are consequences to this).

```js
// Pivot Helper Example
let arr = [5, 2, 1, 8, 4, 7, 6, 3];

pivot(arr); // 4

arr;
// any one of these is an acceptable mutation:
// [2, 1, 4, 3, 5, 8, 7, 6]
// [1, 4, 3, 2, 5, 7, 6, 8]
// [3, 2, 1, 4, 5, 7, 6, 8]
// [4, 1, 2, 3, 5, 6, 8, 7]
// there are other acceptable mutations too.
```

---

### Big O of quickSort

| Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| :--------------------: | :-----------------------: | :---------------------: | :--------------: |
|       O(n log n)       |        O(n log n)         |         O(n^2)          |     O(log n)     |

- O(log n) decompositions
- O(n) comparisons per decomposition
- Worst Case: O(n^2), when the entire array is sorted. We only take the first item each time.
  - O(n) decompositions
  - O(n) comparisons per decomposition
  - Thus, we could pick the middle/median element instead of the first element every time.

---

## Comparison Sorts

- Average Time Complexity
- Best Time Complexity is O(n log n)

| Bubble | Insertion | Selection |   Quick    |   Merge    |
| :----: | :-------: | :-------: | :--------: | :--------: |
| O(n^2) |  O(n^2)   |  O(n^2)   | O(n log n) | O(n log n) |

## Radix Sort

- Not making direct comparisons between 2 elements
  - "Is this number greater than the other number?"
- Radix sort is a special sorting algorithm that works on lists of numbers.
- It exploits the fact that information about the size of a number is encoded in the number of digits
  - More digits means a bigger number.

---

### Radix Sort Helpers (`getDigit`)

- To implement radix sort, need to build a few helper functions first:
  - `getDigit(num, place)`: returns the digit in num at the given place value

```js
getDigit(12345, 0); // 5
getDigit(12345, 1); // 4
```

```js
function getDigit(num, i) {
  return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
}

console.log(getDigit(7323, 2)); // 3
```

### Radix Sort Helpers (`digitCount`)

- `digitCount(num)`: returns the number of digits in num

```js
digitCount(1); // 1
digitCount(25); // 2
digitCount(314); // 3
```

```js
function digitCount(num) {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}
```

### Radix Sort Helpers (`mostDigits`)

- `mostDigits(nums)`: Given an array of numbers, return the number of digits in the largest numbers in the list.

```js
mostDigits([1234, 56, 7]); // 4
mostDigits([1, 1, 11111, 1]); // 5
mostDigits([12, 34, 56, 78]); // 2
```

```js
function mostDigits(nums) {
  let maxDigits = 0;
  for (let i = 0; i < nums.length; i++) {
    maxDigits = Math.max(maxDigits, digitCount(nums[i]));
  }
  return maxDigits;
}
```

### Big O Radix Sort

| Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| :--------------------: | :-----------------------: | :---------------------: | :--------------: |
|         O(nk)          |           O(nk)           |          O(nk)          |     O(n + k)     |

- `n`: length of array
- `k`: number of digits
