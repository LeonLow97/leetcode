# Dijkstra's Algorithm

- Uses Graph and Priority Queue (Binary Heap)
- [Dijkstra's Algorithm Slides](https://cs.slides.com/colt_steele/graphs#/70)

## Objectives

- Understand the importance of Dijkstra's
- Implement a **Weighted Graph**
- Walk through the steps of Dijkstra's
- Implement Dijkstra's using a naive priority queue.
- Implement Dijkstra's using a binary heap priority queue.

## What is Dijkstra's Algorithm?

- Finds the shortest path between 2 vertices on a graph
- "What's the fastest way to get from point A to point B?"

## Why is it useful?

- GPS: finding fastest route
- Network routing: finds open shortest path for data
  - break up messages into a pieces.
- Biology: used to model the spread of viruses among humans
- Airline tickets: finding cheapest route to your destination

## Writing a Weighted Graph

```js
{
    "A": [{node: "B", weight: 10}]
}
```

## Dijkstra's Algorithm Approach

1. Every time we look to visit a new node, we pick the node with the smallest known distance to visit first.
2. Once we've moved to the node we're going to visit, we look at each of its neighbors.
3. For each neighboring node, we calculate the distance by summing the total edges that lead to the node we're checking from the starting node.
4. If the new total distance to a node is less than the previous total, we store the new shorter distance for that node.

<img style="width:50%" src='./dijkstra-algorithm-template.png'>

## Priority Queue

- This priority queue uses the JavaScript sort
  - This gives **time complexity** of O(N log N)

```js
class PriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    this.values.push({ val, priority });
    this.sort();
  }

  dequeue() {
    return this.values.shift();
  }

  sort() {
    this.values.sort((a, b) => a.priority - b.priority);
  }
}
```

## Dijkstra's Algorithm PseudoCode

- This function should accept a starting and ending vertex.
- Create an object (call it "distances") and set each key to be every vertex in the adjacency list with a value of infinity, except for the starting vertex which should have a value of 0.
- After setting a value in the "distances" object, add each vertex with a priority of Infinity to the priority queue, except the starting vertex, which should have a priority of 0 because that's where we begin.
- Create another object called previous and set each key to be every vertex in the adjacency list with a value of null.
- Start looping as long as there is anything in the priority queue
    - dequeue a vertex from the priority queue
    - If that vertex is the same as the ending vertex, we are done!
    - Otherwise loop through each value in the adjacency list at that vertex
        - Calculate the distance to that vertex from the starting vertex
        - If the distance is less that what is currently stored in our distances object,
            - update the distances object with new lower distance
            - update the previous object to contain that vertex
            - enqueue the vertex with the total distance from the start node.


