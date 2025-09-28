// remove PseudoCode
// If the index is less than 0 or greater than or equal to the length, return undefined
// If the index is 0, shift
// If the index is the same as the length - 1, pop
// Use the get method to retrieve the item to be removed.
// Update the next and prev properties to remove the found node from the list
// Set next and prev to null on the found node
// Decrement the length
// Return the removed node

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val) {
    let newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  pop() {
    if (!this.head) {
      return undefined;
    }
    let removedNode = this.tail;
    if (this.length == 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = removedNode.prev;
      this.tail.next = null;
      removedNode.prev = null; // to completely severe ties with the previous node
    }
    this.length--;
    return removedNode;
  }

  shift() {
    if (this.length === 0) {
      return undefined;
    }
    let oldHead = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = oldHead.next;
      this.head.prev = null;
      oldHead.next = null;
    }
    this.length--;
    return oldHead;
  }

  unshift(val) {
    let newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }

  get(index) {
    if (index < 0 || index >= this.length) {
      return null;
    }
    let middle = Math.floor(this.length / 2);
    let count, current;

    if (index < middle) {
      current = this.head;
      count = 0;
      while (count !== index) {
        current = current.next;
        count++;
      }
    }

    if (index >= middle) {
      current = this.tail;
      count = this.length - 1;
      while (count !== index) {
        current = current.prev;
        count--;
      }
    }
    return current;
  }

  set(index, val) {
    let updateNode = this.get(index);
    if (updateNode !== null) {
      updateNode.val = val;
      return true;
    }
    return false;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) {
      return false;
    }
    if (index === 0) {
      return !!this.unshift(val);
    }
    if (index === this.length) {
      return !!this.push(val);
    }
    let prevNode = this.get(index - 1);
    let nextNode = prevNode.next;
    let newNode = new Node(val);

    prevNode.next = newNode;
    newNode.prev = prevNode;
    newNode.next = nextNode;
    nextNode.prev = newNode;
    this.length++;
    return true;
  }

  remove(index) {
    if (index < 0 || index >= this.length) {
      return undefined;
    }
    if (index === 0) {
      return this.shift();
    }
    if (index === this.length - 1) {
      return this.pop();
    }
    let removeNode = this.get(index);

    // removeNode.prev.next = removeNode.next;
    // removeNode.next.prev = removeNode.prev;
    let prevNode = removeNode.prev
    let nextNode = removeNode.next
    prevNode.next = nextNode
    nextNode.prev = prevNode

    removeNode.next = null;
    removeNode.prev = null;

    this.length--;
    return removeNode;
  }
}

let list = new DoublyLinkedList();
list.push(1001);
list.push(1002);
list.push(1003);
list.push(1004);

console.log(list.remove(1));
console.log(list);
