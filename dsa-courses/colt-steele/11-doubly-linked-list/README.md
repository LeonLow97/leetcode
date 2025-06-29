# Doubly Linked List

- [Doubly Linked List Slides](https://cs.slides.com/colt_steele/doubly-linked-lists)
- Each node points in 2 directions.

## Objectives

- Construct a Doubly Linked List
- Compare and contrast Doubly and Singly Linked Lists
- Implement basic operations on a Doubly Linked List.

## What is a Doubly Linked List?

- Almost identical to Singly Linked List, except every node has another pointer to the previous node.
- 2 pointers: next and prev
- Takes up more memory but its more flexible.
  - tradeoff!

## Setup of Doubly Linked List

- Node
  - val, next, prev
- Doubly Linked List
  - head, tail, length

```js
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
}
```

## Doubly Linked List (push)

- Adding a node to the end of the Doubly Linked List

## Doubly Linked List (pop)

- Removing a node from the end of the Doubly Linked List

## Doubly Linked List (shift)

- Removing a node from the beginning of the Doubly Linked List

## Doubly Linked List (unshift)

- Adding a node to the beginning of the Doubly Linked List

## Doubly Linked List (get)

- Accessing a node in a Doubly Linked List by its position

## Doubly Linked List (set)

- Updating the value of a node based on its position in a Doubly Linked List

## Doubly Linked List (insert)

- Adding a node in a Doubly Linked List by a certain position.

## Doubly Linked List (remove)

- Removing a node in a Doubly Linked List by a certain position.

## Doubly Linked List (reverse)

- Reverse a Doubly Linked List

## Big O of Doubly Linked List

| Insertion | Removal | Searching | Access |
| :-------: | :-----: | :-------: | :----: |
|   O(1)    |  O(1)   |   O(N)    |  O(N)  |

- Removal of DLL is faster than that of a SLL.
- Technically searching is O(N/2) but that is still O(N)
  - because we search for the node on both sides. (Divide and Conquer Approach)

## Summary

- Doubly Linked Lists are almost identical to Singly Linked Lists except there is an additional pointer to previous nodes.
- Doubly Linked Lists are used in browsers
    - can use forward and back in web pages
    - doesn't work for singly linked list
- Better than SLL for finding nodes and can be done in half the time (divide and conquer)
- However, DLL do take up more memory considering the extra pointer.


