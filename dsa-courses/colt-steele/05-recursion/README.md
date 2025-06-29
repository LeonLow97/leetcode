# Recursion

- [Recursion Slides](https://cs.slides.com/colt_steele/searching-algorithms-22)

## Objectives

- Define what recursion is and how it can be used.
- Understand the 2 essentials components of a recursive function.
- Visualize the call stack to better debug and understand recursive functions.
- Use helper method recursion and pure recursion to solve more difficult problems.

## Why use Recursion?

- A process (a function in our case) that calls itself.
- `JSON.parse` / `JSON.stringify` are examples of recursive functions.

## The Call Stack

- Built in data structure that manages what happens when functions are invoked.
- **stack data structure**
- Any time a function is invoked, it is placed (**pushed**) on the top of the call stack.
- When JavaScript sees the **return** keyword or when the function ends, the compiler will remove (**pop**).
- When writing **recursive** functions, we keep pushing new functions onto the call stack.

## How recursive function work?

- Invoke the **same** function with a different input until you reach your base case.
- **Base Case**: the condition when the recursion ends.

## 2 essential parts of a recursive function

- Base Case (end point)
- Different Input

## Recursion Pitfalls

- No base case or Wrong base case (code then runs infinitely)
- Forgetting to return or retuning the wrong thing.
  ```js
  function factorial(num) {
    if (num === 1 || num === 0) {
      return 1;
    }
    // did not return factorial(num - 1) instead
    return num * factorial(num);
  }
  ```
- Error Message: Maximum Call Stack Size Exceeded (Stack Overflow)

## Helper Method Recursion

- Helps to persist data
- Defining a recursive funciton inside another function
- E.g., `collectOdds`
- Outer function (which is not recursive) and calls another inner function that is recursive.

```js
function outer(input) {
  var outerScopedVariable = [];

  function helper(helperInput) {
    // modify the outerScopedVariable
    helper(helperInput--);
  }

  helper(input);

  return outerScopedVariable;
}
```

## Pure Recursion

- Inner function is not needed.

## Making Copies

|                Arrays                |                  Objects                  |              Strings               |
| :----------------------------------: | :---------------------------------------: | :--------------------------------: |
|    make copies but do not mutate     | make copies because strings are immutable |       make copies of objects       |
| `slice`, `spread operator`, `concat` |      `slice`, `substr`, `substring`       | `Object.assign`, `spread operator` |
