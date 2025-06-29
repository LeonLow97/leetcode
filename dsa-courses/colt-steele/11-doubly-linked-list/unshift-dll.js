// unshift PseudoCode
// Create a new node with the value passed to the function
// If the length is 0, set the head and tail to be the new node.
// Set the prev property on the head of the list to be the new node.
// Set the next property on the new node to be the head property
// Update the head to be the new node
// Increment the length
// Return the list

class Node {
    constructor(val) {
        this.val = val
        this.next = null
        this.prev = null
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    push(val) {
        let newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
        return this
    }

    pop() {
        if (!this.head) {
            return undefined
        } 
        let removedNode = this.tail
        if (this.length == 1) {
            this.head = null
            this.tail = null
        } else {
            this.tail = removedNode.prev
            this.tail.next = null
            removedNode.prev = null     // to completely severe ties with the previous node
        }
        this.length--
        return removedNode
    }

    shift() {
        if (this.length === 0) {
            return undefined
        }
        let oldHead = this.head
        if (this.length === 1) {
            this.head = null
            this.tail = null
        } else {
            this.head = oldHead.next
            this.head.prev = null
            oldHead.next = null
        }
        this.length--
        return oldHead
    }

    unshift(val) {
        let newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.head.prev = newNode
            newNode.next = this.head
            this.head = newNode
        }
        this.length++
        return this;
    }
}

let list = new DoublyLinkedList()
list.push(99)
list.push(100)
list.push("LAST ITEM")

console.log(list.unshift("ADDED ONE NEW HEAD"))






