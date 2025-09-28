## Python Heap data structure

- Heap data structure is mainly used to represent a **priority queue**.
- In Python, it is available using the `heapq` module.
- The property of this data structure in Python is that each time the smallest heap element is popped (min-heap).
- When elements are pushed or popped, heap structure is maintained.
- The `heap[0]` element returns the smallest element each time.

## Creating a simple heap

- The `heapify(iterable)` function is used to convert the iterable into a heap data structure. Convert to min heap by default.
- Time Complexity: O(n)
  - This method rearranges the elements of the list `li` to satisfy the heap property. The time complexity of `heapify` is linear, proportional to the number of elements in the input list

```py
import heapq

## initialize list
li = [5, 7, 9, 1, 3]

## using heapify to convert list into heap
heapq.heapify(li)

print(list(li)) # Output: [1, 3, 9, 7, 5]
```

## Adding and Popping items efficiently

- `heappush(heap, elem)` function inserts the element into the heap. The order is adjusted, so that the heap structure is maintained.
  - Time Complexity: O(log n)
  - The number of swaps during the bubbling up process is proportional to the height of the heap, which is O(log n)
- `heappop(heap)` function removes and returns the smallest element from the heap. The order is adjusted, so that the heap structure is maintained.
  - Time Complexity: O(log n)
  - The number of swap during the sinking down process is proportional to the height of the heap, which is O(log n).

```py
import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li) # Output: [1, 3, 9, 7, 5]

heapq.heappush(li, 4) # Output: [1, 3, 4, 7, 5, 9]

heapq.heappop(li) # Output: 1
```

## When to apply heap data structure?

1. Find Smallest (or Largest) elements:
   - If the problem involves finding the kth smallest or largest elements from a collection, a min-heap or max-heap can be utilized respectively. Use a min-heap to efficiently extract the smallest elements, or a max-heap for the largest elements.
2. Implementing Priority Queue:
   - When you need to process elements in order of priority (e.g., tasks with different priorities), a priority queue implemented with a heap is an effective choice. It allows quick insertion and retrieval of the highest-priority element.
3. Efficiently handling dynamic priority updates (e.g., Dijkstra's algorithm)
   - If the problem involves dynamically changing priorities (e.g., Dijkstra's algorithm for shortest path), a priority queue can efficiently handle priority updates with heap operations.
4. Merging or handling multiple sorted lists
   - When merging multiple sorted lists or streams of data into a single sorted output, using a heap can streamline the process. The `heapq.merge` function in Python is a good example.
