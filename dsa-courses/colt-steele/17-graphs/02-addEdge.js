/*
- This function should accept 2 vertices, call them vertex1, vertex2.
- The function should find in the adjacency list the key of vertex1 and push vertex2 to the array.
- The function should find in the adjacency list the key of vertex2 and push vertex1 to the array.
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