// piece of data - val
// reference to next node - next
// - This function should accept a value
// - Create a new node using the value passed to the function.
// - If there is no head property on the list, set the head and tail to be the newly created node.
// - Otherwise set the next property on the tail to be the new node and set the tail property on the list to be the newly created node.
// - Increment the length by 1.
// - return the linked list.

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
    // if there is no head property on the list, set the head and tail to be the newly created node.
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      // set the next property on tail to the new node
      this.tail.next = newNode;
      // update the tail to point to the new node ("move" the tail marker)
      this.tail = newNode;
    }
    this.length += 1;
    return this;
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");
console.log(list);
// console.log(list.head)
// console.log(list.head.next);
// console.log(list.head.next.next);

// var first = new Node("Hi")
// first.next = new Node("There")
// first.next.next = new Node("Leon")
// first.next.next.next = new Node("Low")
