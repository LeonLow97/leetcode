<a href="https://cs.slides.com/colt_steele/big-o-notation#/2/0/1">Big O Slides</a>

## Time Complexity Examples

- Suppose we want to write a function that calculates the sum of all numbers from 1 up to (and including) some number n.

- Method 1

```js
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i
    }
    return total;
}
```

- Method 2 (a lot faster - Arithmetic)

```js
function addUpTo(n) {
    return n * (n + 1) / 2
}
```

- Which code is better?
    - Faster?
    - Less memory-intensive?
    - More readable?

- Use timer to compare the performance

```js
let t1 = performance.now();
addUpTo(100000000);
let t2 = performance.now();

console.log(`Time Elaspsed: ${(t2 - t1) / 1000} seconds.`)
```

- The problem with time
    - Different machines will record different times.
    - The same machine will record different times.
    - For fast algorithms, speed measurements may not be precise enough.

- If not time then count what?
    - Let's count the number of simple operations that computer has to perform!

- Counting Operations
    - In method 1, there are n operations because of the for loop. (n additions, n assignments)
        - `+=` and `i++`
        - `5n+2` operations
        - But regardless of the exact number, the number of operations grow proportionally with n.
    - In method 2, there are 3 operations (1 multiplication, 1 addition, 1 division) regardless of the size of n.

<a href="https://rithmschool.github.io/function-timer-demo/">Performance Tracker of the 2 Methods</a>

## Introducing Big O

- Allows us to talk formally about how the runtime of an algorithm grows as the input grows.
- Focus on the broad trends.

- **Defintion**: An algorithm is **O(f(n)) if the number of simple operations the computer has to do is eventually less than a constant times f(n), as n increases.
    - f(n) could be linear (f(n) = n)
    - f(n) could be quadratic (f(n) = n^2)
        - O(n) operation inside of an O(n) operation. (High runtime)
        - E.g. Nested for loops.
    - f(n) could be constant (f(n) = 1)
    - f(n) could be something entirely different

<img src="./big-o-chart.png" alt="Big O Notation Chart" />

- Big O
    - Method 1: O(n)
    - Method 2: O(1)

- Simplifying Big O Notations
    - O(2n) --> O(n)
    - O(500) --> O(1)
    - O(13n^2) --> O(n^2)
    - O(n + 10) --> O(n)
    - O(1000n + 50) --> O(n)
    - O(n^2 + 5n + 8) --> O(n^2)

- Big O Shorthands
    - Arithmetic operations are constants. 
    - Variable assignment is constant.
    - Accessing elements in an array (by index) or object (by key) is constant
    - In a loop, the complexity is the length of the loop times the complexity of whatever happens inside of the loop.
    
## More Examples

- `O(n)`
- Maximum loop is n times.
```js
function logAtLeast5(n) {
    for (var i = 1; i <= Math.max(5, n); i++) {
        console.log(i)
    }
}
```

- `O(1)`
- Maximum loop is 5 times.
```js
function logAtMost5(n) {
    for (var i = 1; i <= Math.min(5, n); i++) {
        console.log(i)
    }
}
```

## Space Complexity

- How can we analyze the runtime of an algorithm as the size of the inputs increases?
- Can use big o notation to analyze the **space complexity**.
- How much additional memory do we need to allocate in order to run the code in our algorithm?

- **Auxiliary Space Complexity** (what we are referring to)
    - Refers to the space required by the algorithm.
    - Not including space taken up by the inputs.

- Space Complexity in JavaScript (Rules of Thumb)
    - Most primitives (booleans, numbers, undefined, null) are constant space.
    - Strings require O(n) space (where n is the string length).
    - Reference types are generally O(n), where n is the length (for arrays) or the number of keys (for objects).

- `O(1) space`
    - Only adding to a variable (variable space stays constant)

```js
function sum(arr) {
    let total = 0 // one number
    for (let i = 0; i < arr.length; i++) {
        total += arr[i]
    }
    return total;
}
```

- `O(n) space`
    - Creating another array. Size of array grows.

```js
function double(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(2 * arr[i]);
    }
    return newArr;
}
```

## Logarithms

- Sometimes big O expressions involve more complex mathematical expressions.
- Inverse of exponential.
- The logarithm of a number roughly measures the number of times you can **divide that number by 2** before you get a value that's less than or equal to 1.

<img src="./how-log-works.png" alt="How Log Works" />
<img src="./log-example.png" alt="Log Example" />

- Using Logarithms
    - Certain searching algorithms have logarithmic time complexity.
    - Efficient sorting algorithms involve logarithms.
    - Recursion sometimes involves logarithmic space complexity.




