# Singly Linked List

- [Singly Linked List Slides](https://nlbsg.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/lecture/8344202#reviews)

## Objectives

- Define what a Singly Linked List is.
- Compare and contrast Linked Lists with Arrays
- Implement insertion, removal and traversal methods on Singly Linked Lists.

## What is a Linked List?

- A data structure that contains a **head, tail and length** property.
- Linked Lists consist of nodes, and each **node** has a **value** and a **pointer** to another node or null.
- Connection of one direction to the next node.

## Comparisons with Arrays

|                    Lists                    |                   Arrays                    |
| :-----------------------------------------: | :-----------------------------------------: |
|             Do not have indexes             |              Indexed in order               |
| Connected via nodes with a **next** pointer |   Insertion and deletion can be expensive   |
|        Random access is not allowed         | Can quickly be accessed at a specific index |

## Singly Linked List (Push)

- Adding a new node to the end of the linked list.

## Singly Linked List (Pop)

- Removing a node from the end of the Linked List.
- Have to assign a new tail when you remove the current tail.
- new tail: second last node.
- Have to traverse the linked list

## Singly Linked List (Shift)

- Removing a new node from the beginning of the Linked List
- Return the old head

## Singly Linked List (Unshift)

- Adding a new node to the beginning of the Linked List.

## Singly Linked List (Get)

- Retrieving a node by it's position in the Linked List.
- Start in the beginning and count how many times we did `.next`
- Not as efficient as an array

## Singly Linked List (Set)

- Changing/Updating the **value** of a node based on it's position in the Linked List.
- Accepts **index** and **value**

## Singly Linked List (Insert)

- Adding a node to the Linked List at a **specific** position.

## Singly Linked List (Remove)

- Removing a node from the Linked List at a **specific** position.

## Singly Linked List (Reverse)

- Reversing the Linked List in place.
- Don't make a copy.
- Traverse and Reverse

<img style="width:60%;" src="./sll-reverse.jpg" alt="Singly Linked List illustration diagram">

## Big O of Singly Linked List

| Insertion |   Reversal    | Searching | Access |
| :-------: | :----------: | :-------: | :----: |
|   O(1)    | O(1) or O(n) |   O(n)    |  O(n)  |

- Reversal
  - O(1) if remove from the beginning
  - O(N) if remove from the end of middle. Have to traverse through the entire linked list
- Searching
  - Traverse through the entire linked list.
- Access
  - Traverse through the entire linked list.
- Accessing an element in ARRAY has a time complexity of O(1), faster than linked list.

## Summary

- Singly Linked Lists are an excellent alternative to arrays when insertion and deletion at the beginning are frequently required.
- Arrays contain a built in index whereas Linked Lists do not.
- The idea of a list data structure that consists of nodes is the foundation for other data structures like Stacks and Queues.

## Practice writing SLL

1. Create a node Class
2. Create a SLL class
3. `push` method
  - add a node the the end of the linked list
  - return SLL
4. `pop` method
  - remove a node from the end of the linked list
  - return the removed node
5. `shift` method
  - remove a node from the beginning of the linked list.
  - return the removed node
6. `unshift` method
  - add a new node to the beginning of the linked list
    - return SLL
7. `get` method
  - retrieving a node by providing it's position in the linked list
  - return node
8. `set` method
  - updating the value of a node based on the index and val
  - return boolean
9. `insert` method
  - adding a node to the specific position of a linked list.
  - return boolean
10. `remove` method
  - remove a node from a list based on provided index.
  - return removed node
11. `reverse` method
  - reversing a linked list
  - return SLL