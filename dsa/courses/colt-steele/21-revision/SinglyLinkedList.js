class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
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
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  pop() {
    if (!this.head) return undefined;

    let current = this.head;
    let newTail = current;
    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    this.tail.next = null;
    current.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }

  shift() {
    if (!this.head) return undefined;
    let removeHead = this.head;
    this.head = this.head.next;
    removeHead.next = null;
    this.length--;
    if (this.length === 0) {
      this.tail = null;
    }
    return removeHead;
  }

  unshift(val) {
    let newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      let oldHead = this.head;
      this.head = newNode;
      this.head.next = oldHead;
    }
    this.length++;
    return this;
  }

  get(index) {
    if (!this.head) return null;
    if (index < 0 || index >= this.length) return null;

    let count = 0;
    let current = this.head;
    while (count !== index) {
      count++;
      current = current.next;
    }
    return current;
  }

  set(index, val) {
    if (!this.head) return false;
    if (index < 0 || index >= this.length) return false;

    let count = 0;
    let current = this.head;
    while (index !== count) {
      count++;
      current = current.next;
    }
    current.val = val;
    return true;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) return false;
    if (index === 0) return !!this.unshift(val);
    if (index === this.length) return !!this.push(val);

    let currentNode = this.get(index - 1);
    let newNode = new Node(val);
    let nextNode = currentNode.next;

    currentNode.next = newNode;
    newNode.next = nextNode;
    this.length++;
    return true;
  }

  //   This function should rotate all the nodes in the list by some number
  //   passed in. For instance, if your list looks like 1 -> 2 -> 3 -> 4 -> 5
  //   and you rotate by 2, the list should be modified to 3 -> 4 -> 5 -> 1 -> 2.
  //   The number passed in to rotate can be any integer.
  rotate(num) {
    let move;
    if (num === 0) return this;
    if (num > 0) move = num % this.length;
    else if (num < 0) move = this.length + (num % this.length)

    for (let i = 0; i < move; i++) {
        this.tail.next = this.head
        this.head = this.head.next
        this.tail = this.tail.next
    }

    this.tail.next = null
    return this;
  }

  print() {
    let arr = [];
    let current = this.head;
    while (current) {
      arr.push(current.val);
      current = current.next;
    }
    return arr;
  }
}

var singlyLinkedList = new SinglyLinkedList();

singlyLinkedList.push(5);
singlyLinkedList.push(10);
singlyLinkedList.push(15);

console.log("Testing push().....");
console.log(singlyLinkedList.length === 3); // 3
console.log(singlyLinkedList.head.val === 5); // 5
console.log(singlyLinkedList.head.next.val === 10); // 10
console.log(singlyLinkedList.head.next.next.val === 15); // 15
console.log(singlyLinkedList.tail.val === 15); // 15

console.log("Testing pop().....");
console.log(singlyLinkedList.pop().val === 15); // 15
console.log(singlyLinkedList.tail.val === 10); // 10
console.log(singlyLinkedList.length === 2); // 2
console.log(singlyLinkedList.pop().val === 10); // 10
console.log(singlyLinkedList.length === 1); // 1
console.log(singlyLinkedList.pop().val === 5); // 5
console.log(singlyLinkedList.length === 0); // 0
console.log(singlyLinkedList.pop() === undefined); // undefined
console.log(singlyLinkedList.length === 0); // 0

singlyLinkedList.push(5);
singlyLinkedList.push(10);
singlyLinkedList.push(15);
singlyLinkedList.push(20);
console.log("Testing get().....");
console.log(singlyLinkedList.get(0).val === 5); // 5
console.log(singlyLinkedList.get(1).val === 10); // 10
console.log(singlyLinkedList.get(2).val === 15); // 15
console.log(singlyLinkedList.get(3).val === 20); // 20
console.log(singlyLinkedList.get(4) === null); // null

console.log("Testing set().....");
console.log(singlyLinkedList.set(0, 10)); // true
console.log(singlyLinkedList.set(1, 2)); // true
console.log(singlyLinkedList.length === 4); // 2
console.log(singlyLinkedList.head.val === 10); // 10
console.log(singlyLinkedList.set(10, 10) === false); // false
console.log(singlyLinkedList.set(3, 100)); // true
console.log(singlyLinkedList.head.next.next.next.val === 100); // 100

console.log("Testing insert().....");
var singlyLinkedList = new SinglyLinkedList();
singlyLinkedList.push(5).push(10).push(15).push(20);
console.log(singlyLinkedList.insert(2, 12) === true); // true
console.log(singlyLinkedList.insert(100, 12) === false); // false
console.log(singlyLinkedList.length === 5); // 5
console.log(singlyLinkedList.head.val === 5); // 5
console.log(singlyLinkedList.head.next.val === 10); // 10
console.log(singlyLinkedList.head.next.next.val === 12); // 12
console.log(singlyLinkedList.head.next.next.next.val === 15); // 15
console.log(singlyLinkedList.head.next.next.next.next.val === 20); // 20
console.log(singlyLinkedList.insert(5, 25)); // true
console.log(singlyLinkedList.head.next.next.next.next.next.val === 25); //25
console.log(singlyLinkedList.tail.val === 25); // 25

var singlyLinkedList = new SinglyLinkedList();
singlyLinkedList.push(1).push(2).push(3).push(4).push(5);
console.log(singlyLinkedList.rotate(-1).print());

var singlyLinkedList = new SinglyLinkedList();
singlyLinkedList.push(1).push(2).push(3).push(4).push(5);
console.log(singlyLinkedList.rotate(1).print());
