// Get PseudoCode
// The function should accept an index.
// If the index is less than 0 or greater than or equal to the length of the list, return null
// Loop though the list until you reach the index and
// return the node at that specific index.

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
    return current
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");

console.log("[get()]", list.get(0));
console.log("[get()]", list.get(1));
console.log("[get()]", list.get(2));
console.log("[get()]", list.get(-1));