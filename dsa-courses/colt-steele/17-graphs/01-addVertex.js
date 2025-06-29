/*
- Write a method called `addVertex`, which accepts the name of a vertex.
- It should add a key to the adjacency list with the name of the vertex and set its value to be an empty array.
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
}

let g = new Graph()
g.addVertex("Tokyo")
g.addVertex("Singapore")
g.addVertex("Singapore")
console.log(g)