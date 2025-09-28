# Sorting Algorithms

- [Sorting Algorithms Slides](https://cs.slides.com/colt_steele/elementary-sorting-algorithms)
- [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)

## Objectives

- Implement bubble sort
- Implement selection sort
- Implement insertion sort
- Understand why it is important to learn these simpler sorting algorithms.

## What is sorting?

- Sorting is the process of rearranging the items in a collection (e.g., an array) so that the items are in some kind of order.
- Examples
  - Sorting numbers from smallest to largest
  - Sorting names alphabetically
  - Sorting movies based on release year
  - Sorting movies based on revenue

## Why sorting?

- Sorting is a common task.
- There are many different ways to sort things, and different techniques have their own advantages and disadvantages.

## Built-in JavaScript `sort()` method

```js
// Sorted alphabetically
["Steele", "Colt", "Data Structures", "Algorithms"]
  .sort() // ["Algorithms", "Colt", "Data Structures", "Steele"]

  [
    // Not exactly what we want when sorting numerically
    (6, 4, 15, 10)
  ].sort(); // [10, 15, 4, 6]
```

## Telling JavaScript how to sort

- The built-in sort method accepts an optional _comparator_ function.
- Can use this comparator function to tell JavaScript how you want it to sort
- The comparator looks at pairs of elements (a and b), determines their sort order based on the return value.
  - If it returns a negative number, a should come before b.
  - If it returns a positive number, a should come after b.
  - If it returns 0, a and b are the same as far as the sort is concerned.

## Bubble Sort

- Not very efficient (rarely implemented)
- A sorting algorithm where the largest values "bubble" up to the top.
- Good for data that is nearly sorted

```js
/*
[5,3,4,1,2] // compares 5 and 3
[3,5,4,1,2] // compares 5 and 4
[3,4,5,1,2]
[3,4,1,5,2]
[3,4,1,2,5] // sorted '5'
*/
```

- Before we sort, we must swap
- Many sorting algorithms involve some type of swapping functionality (e.g., swapping 2 numbers to ut them in order).

```js
// ES5 (Recommended)
function swap(arr, idx1, idx2) {
  var temp = arr[idx1];
  arr[idx1] = arr[idx2];
  arr[idx2] = temp;
}

// ES2015
const swap = (arr, idx1, idx2) => {
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
};
```

- **Time Complexity**
  - Worst Case: O(N^2)
  - Best Case: If data is nearly sorted, it will be O(N)

## Selection Sort

- Similar to bubble sort, but instead of first placing large values into sorted position, it places small values into sorted position.
- Does not perform well on data that is nearly sorted.

```js
/*
// find the minimum and put in the beginning
// Compare '5' with the rest first and find if any number if smaller than 5 then swap
[5,3,4,1,2]
[1,3,4,5,2]
*/
```

- **Time Complexity**
  - O(N^2)

## Insertion Sort

- Builds up the sort by gradually creating a larger left half which is always sorted.
- Good for data that is nearly sorted

```js
/*
[5,3,4,1,2] 
[3,5,4,1,2] 
[3,4,5,1,2]
[1,3,4,5,2]
[1,2,3,4,5]
*/
```

- Time Complexity

  - Worst Case: O(N^2)
    - Worst Case Scenario ([4,3,2,1])
  - Best Case: O(N), data is nearly sorted

- If data is coming in live and you need to insert it, insertion sort is good because one side is already sorted and can just keep inserting.
- Insertion sort is good if you need data to be **continuously sorted**.

-----

- Take the 'right' value and check if 'left' value is greater than the 'right'.
  - [2, 1, 3]
- If greater, make a copy of 'left' value to the index position of 'right' value.
  - [2, 2, 3]
- Once iterating to the left is complete, attach the `currentVal` to the position.
  - [1, 2, 3]
- <img src="./insertionSort.jpg" alt="illustration of insertion sort drawn by leon low">

## Comparing Bubble, Insertion and Selection Sort

|   Algorithm    | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| :------------: | :--------------------: | :-----------------------: | :---------------------: | :--------------: |
|  Bubble Sort   |          O(N)          |          O(N^2)           |         O(N^2)          |       O(1)       |
| Insertion Sort |          O(N)          |          O(N^2)           |         O(N^2)          |       O(1)       |
| Selection Sort |         O(N^2)         |          O(N^2)           |         O(N^2)          |       O(1)       |
