// BST Insert
/*
- Create a new node
- Starting at the root
    - Check if there is a root, if not - the root now becomes that new model.
    - If there is a root, check if the value of the new node is greater than or less than the value of the root.
    - If it is greater
        - Check to see if there is a node to the right
            - If there is, move to that node and repeat these steps.
            - If there is not, add that node as the right property
    - If it is less
        - Check to see if there is a node to the left
            - If there is, move to that node and repeat these steps.
            - If there is not, add that node as the left property
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
        if (val === current.val) return undefined
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
      // while (true) {
      //   if (val === current.val) return undefined
      //   if (val < current.val) {
      //     if (current.left === null) {
      //       current.left = newNode
      //       return this;
      //     }
      //     current = current.left
      //   } else {
      //     if (current.right === null) {
      //       current.right = newNode
      //       return this;
      //     }
      //     current = current.right
      //   }
      // }
    }
  }
}

let tree = new BinarySearchTree();
console.log(tree.insert(10));
console.log(tree.insert(5));
console.log(tree.insert(13));
console.log(tree.insert(11));
console.log(tree.insert(2));
console.log(tree.insert(16));
console.log(tree.insert(7));

console.log(tree);

/*
        10
    5       13
  2   7   11   16
*/
