# Tree Traversal

- [Tree Traversal Slides](https://cs.slides.com/d/SAf3EIc/live#/40)

## Traversing a Tree

- Breadth First Search (BFS): horizontal
- Depth First Search (DFS): vertical
  - InOrder
    - InOrder Traversal is the one the most used variant of DFS(Depth First Search) Traversal of the tree.
    - An InOrder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).
    - Everything is arranged in order. smallest to largest in the array.
  - PreOrder
    - PreOrder means we visit the node before visiting its children. 
  - PostOrder
    - PostOrder order means we visit the node only after visiting its children.
- Nodes on the left are smaller than nodes on the right.
- Summary
  - Inorder => Left, Root, Right
  - Preorder => Root, Left, Right
  - Postorder => Left, Right, Root

---

# Breadth First Search (BFS)

## BFS (Steps - Iteratively)

- Create a queue (this can be an array) and a variable to store the values of nodes visited.
- Place the root node in the queue
- Loop as long as there is anything in the queue.
  - Dequeue a node from the queue and push the value of the node into the variable that stores the nodes.
  - If there is a left property on the node dequeued - add it to the queue.
  - If there is a right property on the node dequeued - add it to the queue.
- Return the variable that stores the values.

---

# Depth First Search (DFS)

## DFS PreOrder (Steps - Recursively)

- Create a variable to store the values of nodes visited.
- Store the root of the BST in a variable called current.
- Write a helper function which accepts a node
  - Push the value of the node to the variable that stores the values.
  - If the node has a left property, call the helper function with the left property on the node.
  - If the node has a right property, call the helper function with the right property on the node.
- Invoke the helper function with the current variable.
- Return the array of values.

## DFS PostOrder (Steps - Recursively)

- Create a variable to store the values of nodes visited.
- Store the root of the BST in a variable called current.
- Write a helper function which accepts a node.
  - If the node has a left property, call the helper function with the left property on the node.
  - If the node has a right property, call the helper function with the right property on the node.
  - Push the value of the node to the variable that stores the values
  - Invoke the helper function with the current variable.
- Return the array of values.

## DFS InOrder (Steps - Recursively)

- Create a variable to store the values of nodes visited.
- Store the root of the BST in a variable called current.
- Write a helper function which accepts a node.
  - If the node has a left property, call the helper function with the left property on the node.
  - Push the value of the node to the variable that stores the values
  - If the node has a right property, call the helper function with the right property on the node.
  - Invoke the helper function with the current variable.
- Return the array of values.

## Which one is better? BFS? DFS?

- If there are lots of nodes, time complexity is the same but space complexity is not.
    - we have to store a ton of data in the 'queue' in BFS. High space complexity needed to store.
    - DFS would use less space than BFS in this case.
- DFS InOrder
    - Used commonly with BST's
    - Notice we get all the nodes in the tree in their underlying order.
- DFS PreOrder
    - Can be used to "export" a tree structure so that it is easily reconstructed or copied.
    - Starts off with a root.
- However, it is easy to switch between the different methods of DFS.
- The real concern is between BFS and DFS.

## Summary

- Trees are non-linear data structures that contain a root and child nodes.
- Binary Trees can have values of any type, but at most 2 children for each parent.
- Binary Search Trees are a more specific version of binary trees where every node to the left of a parent is less than it's value and every node to the right is greater.
- Can search through Trees using BFS and DFS.


