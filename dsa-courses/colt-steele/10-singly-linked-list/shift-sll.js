// Shifting PseudoCode
// If there are no nodes, return undefined
// Store the current head property in a variable
// Set the head property to be the current head's next property
// Decrement the length by 1
// Return the value of the node removed

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
    this.length++;
    return this;
  }

  shift() {
    if (!this.head) {
      return "The Singly Linked List has no nodes!";
    }
    let currentHead = this.head;
    this.head = currentHead.next;
    this.length--;
    if (this.length === 0) {
      this.tail = null;
    }
    return currentHead;
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");

console.log("[SLL]:", list);

console.log("[shift()]:", list.shift());
console.log("[SLL]:", list);

// console.log("[shift()]:", list.shift())
// console.log("[SLL]:", list)

// console.log("[shift()]:", list.shift())
// console.log("[SLL]:", list)

// console.log("[shift()]:", list.shift())
// console.log("[SLL]:", list)
