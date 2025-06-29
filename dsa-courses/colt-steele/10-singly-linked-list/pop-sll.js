// Popping PseudoCode
// If there are no nodes in the list, return undefined
// Loop through the list until you reach the tail
// Set the next property of the 2nd to last node to be null
// Set the tail to be the 2nd to last node
// Decrement the length of the list by 1
// Return the value of the node removed

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

// console.log(first)

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

  pop() {
    // check if there no nodes (can also check if length is 0)
    if (!this.head) {
      return "The Singly Linked List has no nodes!";
    }
    let current = this.head;
    let newTail = current;
    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    this.tail.next = null;
    this.length--;
    // popped the last item off
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");
// console.log(list);

console.log("[SLL pop()]:", list.pop());
console.log("[SLL]:", list);

// // Testing out popping off everything in the SLL
// console.log("[SLL pop()]:", list.pop());
// console.log("[SLL pop()]:", list.pop());
// console.log("[SLL]:", list);
// console.log("[SLL pop()]:", list.pop());
// console.log("[SLL]:", list);


