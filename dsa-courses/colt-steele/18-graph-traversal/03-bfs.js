class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
    }
  }

  addEdge(vertex1, vertex2) {
    if (this.adjacencyList[vertex1]) {
      this.adjacencyList[vertex1].push(vertex2);
    }
    if (this.adjacencyList[vertex2]) {
      this.adjacencyList[vertex2].push(vertex1);
    }
  }

  DFS_recursive(start) {
    const result = [];
    const visited = {};
    const adjacencyList = this.adjacencyList;

    function DFS(vertex) {
      if (!vertex) return null;
      visited[vertex] = true;
      result.push(vertex);
      adjacencyList[vertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          return DFS(neighbor);
        }
      });
    }
    DFS(start);
    return result;
  }

  DFS_iterative(start) {
    let stack = [];
    let result = [];
    let visited = {};
    const adjacencyList = this.adjacencyList;

    stack.push(start);
    visited[start] = true;

    while (stack.length > 0) {
      // console.log(stack)
      let currentVertex = stack.pop();
      result.push(currentVertex);

      this.adjacencyList[currentVertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          stack.push(neighbor);
        }
      });
    }
    return result;
  }

  BFS(start) {
    const queue = [];
    const result = [];
    const visited = {};

    queue.push(start);
    visited[start] = true;

    while (queue.length > 0) {
      let currentVertex = queue.shift();    // instead of pop()
      result.push(currentVertex);

      this.adjacencyList[currentVertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          queue.push(neighbor);
        }
      });
    }
    return result;
  }
}

let g = new Graph();
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");
g.addVertex("D");
g.addVertex("E");
g.addVertex("F");

g.addEdge("A", "B");
g.addEdge("A", "C");
g.addEdge("B", "D");
g.addEdge("C", "E");
g.addEdge("D", "E");
g.addEdge("D", "F");
g.addEdge("E", "F");

console.log(g);
console.log("DFS Recursive", g.DFS_recursive("A"));
console.log("DFS Iterative", g.DFS_iterative("A"));
console.log("BFS", g.BFS("A"));
