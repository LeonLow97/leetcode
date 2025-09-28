class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class Stack {
    constructor() {
        this.first = null
        this.last = null
        this.size = 0
    }

    push(val) {
        let newNode = new Node(val)
        if (this.size == 0) {
            this.first = newNode
            this.last = newNode
        } else {
            let firstElem = this.first
            this.first = newNode
            newNode.next = firstElem
        }
        return ++this.size
    }

    pop() {
        if (!this.first) {
            return null
        }
        let temp = this.first
        if (this.size === 1) {
            this.first = null
            this.last = null
        } else {
            this.first = this.first.next
            temp.next = null
        }
        this.length--
        return temp.val
    }
}

let stack = new Stack()
console.log(stack.push("FIRST"))
console.log(stack.push("SECOND"))
console.log(stack.push("THIRD"))
console.log(stack.push("LAST"))
console.log(stack.pop())