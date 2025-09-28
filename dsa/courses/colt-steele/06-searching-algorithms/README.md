# Searching Algorithms

- [Searching Algorithms Slides](https://cs.slides.com/colt_steele/tries-21)

## Objectives

- Describe what a searching algorithm is
- Implement linear search on arrays
  - search one by one
  - `indexOf`, `includes`, `find`, `findIndex`
- Implement binary search on sorted arrays
- Implement a naive string searching algorithm
- Implement the KMP string searching algorithm

## Linear Search

- Given an array, the simplest way to search for a value is to look at every element in the array and check if it's the value we want.
- Start at the beginning or start at the end and check every single element.
- Time Complexity:
  - Best Case: O(1)
  - Worst Case: O(N)

## Binary Search (Divide and Conquer)

- Binary search is much faster form of search
- Rather than eliminating one element at a time, you can eliminate half of the remaining elements at a time.
- Binary search only works on **sorted** arrays.

## Binary Search (Big O)

- Time Complexity:
  - Best Case: O(1), middle point is the number we are looking for.
  - Worst and Average Case: O(log N) --> Very Good, almost similar to O(1) in the time complexity graph.

## Naive String Search

- Suppose you want to count the number of times a smaller string appears in a longer string.
- A straightforward approach involves checking pairs of characters individually.


