// Insert PseudoCode
// If the index is less than 0 or greater than the length, return false.
// If the index is the same as the length, push a new node to the end of the list.
// If the index is 0, unshift a new node to the start of the list
// Otherwise, using the get method, access the node at the index -1
// Set the next property on the node to be the new node.
// Set the next property on the new node to be the previous next
// Increment the length
// Return true

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
    let node = this.get(index);
    if (!node) {
      return false;
    }
    node.val = val;
    return true;
  }

  unshift(val) {
    let newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      // only runs when there is a node in the SLL
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) {
      return false;
    }
    if (index === this.length) {
      return !!this.push(val);
    }
    if (index === 0) {
      return !!this.unshift(val);
    }

    let newNode = new Node(val);
    let prevNode = this.get(index - 1);
    let temp = prevNode.next;

    prevNode.next = newNode;
    newNode.next = temp;

    this.length++;
    return true;
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");

console.log("[insert()]:", list.insert(0, "Inserting at the beginning..."));
console.log(list);

console.log("[insert()]:", list.insert(1, "Inserting at index 1..."));
console.log(list);

console.log("[insert()]:", list.insert(5, "Inserting at the end..."));
console.log("[SLL index 5]:", list.get(5));

// console.log("[insert()]:", list.insert(3, "Inserting at the end..."))
// console.log(list)
