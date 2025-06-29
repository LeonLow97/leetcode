# Stacks

- [Stacks Slides](https://cs.slides.com/colt_steele/stacks)

## Objectives

- Define what a stack is
- Understand use cases for a stack
- Implement operations on a stack data structure

## What is a stack?

- A LIFO data structure (where the last value in is always the first one out)
- The last element added to the stack will be the first element to be removed from the stack.
- E.g., _Call Stack_

## Where stacks are used

- Managing function invocations
- Undo/redo e.g., photo-shopping
- Routing (the history object - frontend) is treated like a stack
  - pages viewed

## Implementing a stack

- There is more than 1 way of implementing a stack.
- _Array_ Implementation
  - `.push()` and `.pop()`
    - better option: does not require re-indexing.
  - `.unshift()` and `.shift()`
    - might not be good to use this because adding to the beginning of an array is O(N)
    - have to re-index every element.
  - using array to implement a stack might not be efficient, use linked list instead
- _Linked List_ Implementation
  - `stack.push()` and `stack.pop()`
  - add node to beginning and remove node from the beginning of linked list.

### `Pushing` PseudoCode

- `push` to the beginning of the linked list.
- Similar to SLL unshift
  - Did not use SLL push and pop because pop requires us to traverse through the entire linked list as this is done at the end of the linked list.
- The function should accept a value.
- Create a new node with that value
- If there are no nodes in the stack, set the first and last property to be the newly created node.
- If there is at least 1 node, create a variable that stores the current first property on the stack.
- Reset the first property to be the newly created node
- Set the next property on the node to be the previously created variable.
- Increment the size of the stack by 1.

### `Pop` PseudoCode

- `pop` remove from the beginning of linked list
- If there are no nodes in the stack, return null.
- Create a temporary variable to store the first property on the stack.
- If there is only 1 node, set the first and last property to be null.
- If there is more than 1 node, set the first property to be the next property on the current first.
- Decrement the size by 1.
- Return the value of the node removed.

## Big O of Stacks

| Insertion | Removal | Searching | Access |
| :-------: | :-----: | :-------: | :----: |
|   O(1)    |  O(1)   |   O(N)    |  O(N)  |

# Queues

- [Queues Slides](https://cs.slides.com/colt_steele/queues)

## Objectives

- Define what a queue is
- Understand use cases for a queue
- Implement operations on a queue data structure

## What is a Queue?

- FIFO (First in first out) data structure.
- Examples
  - Background tasks
  - Uploading resources
  - Printing / Task processing

## Implementation

- Building a queue with an array
  - not efficient as it requires re-indexing of every element when we add to the beginning of the array.
- Queue class
  - `enqueue` and `dequeue`
  - add node to the tail and remove node from the head of the linked list.

```js
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
}
```

## Big O of Queues

| Insertion | Removal | Searching | Access |
| :-------: | :-----: | :-------: | :----: |
|   O(1)    |  O(1)   |   O(N)    |  O(N)  |

## Summary

- Stacks: add node to beginning and remove node from the beginning of linked list.
- Queue: add node to the tail and remove node from the head of the linked list.
