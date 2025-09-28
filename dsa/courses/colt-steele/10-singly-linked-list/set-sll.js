// Set PseudoCode
// This function should accept a value and an index.
// Use the get function to find the specific node.
// If the node is not found, return false.
// If the node is found, set the value of that node to be the value
// passed to the function and return true.

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class singlyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val) {
    let newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length += 1;
    return this;
  }

  get(index) {
    if (!this.head) {
      return "The Singly Linked List has no nodes!";
    }
    if (index < 0 || index >= this.length) {
      return null;
    }
    let count = 0;
    let current = this.head;
    while (count !== index) {
      current = current.next;
      count++;
    }
    return current;
  }

  set(index, val) {
    let node = this.get(index)
    if (!node) {
        return false
    } 
    node.val = val
    return true
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");

console.log("[set()]", list.set(1, "Jie Wei"))
console.log("[get()]", list.get(1))
