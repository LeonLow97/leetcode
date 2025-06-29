class PriorityQueue {
    constructor() {
        this.values = []
    }

    enqueue(val, priority) {
        this.values.push({val, priority})
        this.sort()
    }

    dequeue() {
        return this.values.shift()
    }

    sort() {
        this.values.sort((a, b) => a.priority - b.priority)
    }
}

let pq = new PriorityQueue()
pq.enqueue("A", 20)
pq.enqueue("B", 23)
pq.enqueue("C", 14)
pq.enqueue("D", 1)

console.log(pq)

console.log(pq.dequeue())