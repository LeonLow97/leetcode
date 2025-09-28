// get PseudoCode
// If the index is less than 0 or greater or equal to the length, return null
/* If the index is less than or equal to half the length of the list,
        - Loop through the list starting from the head and loop towards the middle.
        - Return the node once it is found
*/
/* If the index is greater than half the length of the list,
        - Loop through the list starting from the tail and loop towards the middle.
        - Return the node once it is found
*/

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

    get(index) {
        if (index < 0 || index >= this.length) {
            return null
        }
        let middle = Math.floor(this.length / 2)
        let count, current;

        if (index < middle) {
            console.log("WORKING FROM BEGINNING")
            current = this.head
            count = 0
            while (count !== index) {
                current = current.next
                count++
            }
        }

        if (index >= middle) {
            console.log("WORKING FROM END")
            current = this.tail
            count = this.length - 1
            while (count !== index) {
                current = current.prev
                count--
            }
        }
        return current
    }
}

let list = new DoublyLinkedList()
list.push(99)
list.push(100)
list.push(101)
list.push(102)
list.push("LAST ITEM")

console.log(list.get(5))






