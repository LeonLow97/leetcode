// shift PseudoCode
// If the length is 0, return undefined
// Store the current head property in a variable
// If the length is 1, set the head to be null and the tail to be null
// Update the head to be the next of the old head
// Set the head's prev property to null
// Set the old head's next to null
// Decrement the length
// Return old head

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
}

let list = new DoublyLinkedList()
list.push(99)
list.push(100)
list.push("LAST ITEM")

console.log(list.shift())
console.log("[DLL]", list)






