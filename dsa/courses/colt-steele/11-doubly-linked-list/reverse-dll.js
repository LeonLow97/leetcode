// Reverse PseudoCode

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

  pop() {
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
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return current;
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

  remove(index) {
    if (index < 0 || index > this.length) {
      return "Index out of range!";
    }
    if (index === this.length - 1) {
      // last element
      return this.pop();
    }
    if (index === 0) {
      return this.shift();
    }
    let prevNode = this.get(index - 1);
    let removeNode = prevNode.next;
    prevNode.next = removeNode.next;
    this.length--;
    return removeNode;
  }

  reverse() {
    let node = this.head;
    this.head = this.tail
    this.tail = node
    
    let nextNode = null
    let prevNode = null

    for (let i = 0; i < this.length; i++) {
        nextNode = node.next
        node.next = prevNode
        node.prev = nextNode
        prevNode = node
        node = nextNode
    }
    return this;
  }
}

var list = new singlyLinkedList();
list.push("Hello");
list.push("Leon");
list.push("Low");

console.log(list.reverse())
