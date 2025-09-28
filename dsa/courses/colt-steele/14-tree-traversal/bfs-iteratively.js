// BFS (Steps - Iteratively)
/*
- Create a queue (this can be an array) and a variable to store the values of nodes visited.
- Place the root node in the queue
- Loop as long as there is anything in the queue.
    - Dequeue a node from the queue and push the value of the node into the variable that stores the nodes.
    - If there is a left property on the node dequeued - add it to the queue.
    - If there is a right property on the node dequeued - add it to the queue.
- Return the variable that stores the values.
*/

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(val) {
    let newNode = new Node(val);
    if (!this.root) {
      this.root = newNode;
      return this;
    } else {
      let current = this.root;
      while (true) {
        if (val === current.val) return undefined;
        if (val < current.val) {
          if (current.left === null) {
            current.left = newNode;
            return this;
          } else {
            current = current.left;
          }
        } else if (val > current.val) {
          if (current.right === null) {
            current.right = newNode;
            return this;
          } else {
            current = current.right;
          }
        }
      }
    }
  }

  BFS() {
    let queue = [];
    let visited = [];
    let node = this.root;

    if (!this.root) {
      return false;
    } else {
      queue.push(node);
    }

    while (queue.length > 0) {
      node = queue.shift();
      visited.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
      
    }
    return visited;
  }
}

let tree = new BinarySearchTree();
tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(11);
tree.insert(2);
tree.insert(16);
tree.insert(7);

console.log(tree.BFS()); // [10, 5, 13, 2, 7, 11, 16]

/*
          10
      5       13
    2   7   11   16
  */
