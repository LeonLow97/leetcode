/*
- This function should accept 2 values, vertex1 and vertex2.
- The function should reassign the key of vertex1 to be an array that does not contain vertex2.
- The function should reassign the key of vertex2 to be an array that does not contain vertex1.
- Don't worry about handling errors/invalid vertices.
*/

class Graph {
    constructor() {
        this.adjacencyList = {}
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = []
        }
    }

    addEdge(vertex1, vertex2) {
        if (this.adjacencyList[vertex1]) {
            this.adjacencyList[vertex1].push(vertex2)
        }
        if (this.adjacencyList[vertex2]) {
            this.adjacencyList[vertex2].push(vertex1)
        }
    }

    removeEdge(vertex1, vertex2) {
        // let idx1 = this.adjacencyList[vertex1].indexOf(vertex2)
        // if (idx1 > -1) {
        //     this.adjacencyList[vertex1].splice(idx1, 1)
        // }

        // let idx2 = this.adjacencyList[vertex2].indexOf(vertex1)
        // if (idx2 > -1) {
        //     this.adjacencyList[vertex2].splice(idx2, 1)
        // }
        this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(v => v !== vertex2)
        this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(v => v !== vertex1)
    }
}

let g = new Graph()
g.addVertex("Tokyo")
g.addVertex("Singapore")
g.addVertex("Singapore")
g.addVertex("Malaysia")
console.log(g)

g.addEdge("Tokyo", "Singapore")
g.addEdge("Singapore", "Malaysia")

console.log(g)

g.removeEdge("Tokyo", "Singapore")

console.log(g)