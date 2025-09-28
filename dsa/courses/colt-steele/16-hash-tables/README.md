# Hash Tables / Hash Map

- [Hash Tables Slides](https://cs.slides.com/colt_steele/hash-tables)

## Objectives

- Explain what a hash table is
- Define what a hashing algorithm is
- Discuss what makes a good hashing algorithm
- Understand how collisions occur in a hash table
- Handle collisions using separate chaining or linear probing.

## What is a hash table?

- Hash tables are used to store _key-value_ pairs.
- They are like arrays, but the keys are not ordered.
- Unlike arrays, hash tables are fast for all of the following operations:
  - find values, adding new values, and removing values.

## Uses of hash table

- Nearly every programming language has some sort of hash table data structure.
  - Python has Dictionaries
  - JavaScript has Objects and Maps
- Because of their speed, hash tables are very commonly used.

## key-value pair

- Object[key] = value

## Hash Part

- To implement a hash table, use an array.
- In order to **look up values by key**, we need a way to convert keys into valid array **indices**.
  - A function that performs this task is called a **hash function**.

## Uses of Hash Function

- Used in cryptocurrency, cryptographic, password validation

## What makes a good hash?

1. Fast (i.e. constant time)
1. Doesn't cluster outputs at specific, but distribute values uniformly.
1. Deterministic (same input yields same output)

## Examples of Bad Hash Functions

```js
// Hash should be fast
function slowHash(key) {
  for (var i = 0; i < 10000; i++) {
    console.log("everyday i'm hashing");
  }
  return key[0].charCodeAt(0);
}

// Hash should uniformly distribute values
function sameHashedValue(key) {
  return 0;
}

// Hash should be deterministic
function randomHash(key) {
  return Math.floor(Math.random() * 1000)
}
```

## Implementing the Hash Function on **Strings**

- Hash that works on string only
- However, the following hash functions has a few issues:
    - Only hashes strings
    - Not constant time - linear in key length
    - Could be a little more random
```js
function hash(key, arrayLen) {
  let total = 0;
  for (let char of key) {
    // map "a" to 1, "b" to 2, "c" to 3, etc.
    let value = char.charCodeAt(0) - 96
    total = (total + value) % arrayLen;
  }
  return total;
}
```

## Adding Prime Numbers to the Hash Function

- The prime number in the hash is helpful in spreading out the keys more uniformly.
- It's also helpful if the array that you're putting values into has a prime length.
- Don't need to know why (Math is complicated).

```js
function hash(key, arrayLen) {
  let total = 0;
  let WEIRD_PRIME = 31;
  for (let i = 0; i < Math.min(key.length, 100); i++) {
    let char = key[i];
    let value = char.charCodeAt(0) - 96
    total = (total * WEIRD_PRIME + value) % arrayLen;
  }
  return total;
}
```

## Dealing with Collisions

- Even with a large array and a great hash function, collisions are inevitable.
- There are many strategies for dealing with collisions, but we will focus on 2:
    - Separate Chaining
    - Linear Probing
        - limited to defined array size
    
-----

### Separate Chaining

- With separate chaining, at each index in our array, we store values using a more sophisticated data structure (e.g., an array or a linked list).
- This allows us to store multiple key-value pairs at the same index.

<img style="width:40%" src="./separate-chaining.png" alt="Separate Chaining Diagram">

-----

### Linear Probing

- With linear probing, when we find a collision, we search through the array to find the next empty slot.
- Unlike with separate chaining, this allows us to store a single key-value at each index.

<img style="width:40%" src="./linear-probing.png" alt="Separate Chaining Diagram">

## Set / Get Methods

-----

### Set

1. Accepts a key and a value
2. Hashes the key
3. Stores the key-value pair in the hash table array via **separate chaining**.

### Get

1. Accepts a key
2. Hashes the key
3. Retrieves the key-value pair in the hash table.
4. If the key isn't found, return undefined.

## Keys / Values

-----

### keys

1. Loop through the hash table array and return an array of keys in the table.
1. Check for duplicate data

### values

1. Loop through the hash table array and return an array of values in the table.

## Big O of Hash Tables

### Average Case

|Insert|Deletion|Access|
|:-:|:-:|:-:|
|O(1)|O(1)|O(1)|

### Worst Case

- O(n)
  - all key-values belong in the same hash
