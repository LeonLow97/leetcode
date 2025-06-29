# Lessons learnt in Python

- sorted() vs sort()
- Looping with enumerate.

## sorted() vs sort()

## Looping with enumerate

## Reversing a list in Python

- x = [5,4,3,2,1]
- `x[::-1]` returns [1,2,3,4,5]

## Why is the space complexity of a recursive inorder tree traversal O(H) amd not O(N)?

- [StackOverflow Explanation](https://stackoverflow.com/questions/41201908/why-is-the-space-complexity-of-a-recursive-inorder-traversal-oh-and-not-on)
- During the traversal of nodes recursively, we push the node's memory address to the call stack.
- However, the addresses are removed from the stack when **returning**.
- The space is re-used when making a new call from a level closer to the root.
- So, the maximum numbers of memory addresses on the stack at the same time is the tree height.

```
# Number of nodes, n = 4
# Number of stack frames requires in recursive traversal = 4
  1
 / \
    2
   / \
      3
     / \
        4
```

## 