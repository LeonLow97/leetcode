// Insert PseudoCode
/*
- Push the value into the values property on the heap.
- Bubble the value up to its correct spot.
    - Bubble Up:
        - Create a variable called index which is the length of the values property - 1
        - Create a variable called parentIndex which is the floor of (index - 1) / 2
        - Keep looping as long as the values element at the parentIndex is less than the values element at the child index.
            - Swap the value of the values element at the parentIndex with the value of the element property at the child index.
            - Set the index to be the parentIndex, and start over.
*/

class MaxBinaryHeap {
  constructor() {
    // assume starting heap has these values
    this.values = [41, 39, 33, 18, 27, 12];
  }

  bubbleUp() {
    let idx = this.values.length - 1;
    const element = this.values[idx];
    while (idx > 0) {
      // need to ensure idx > 0 otherwise the statement below might bring index to negative
      let parentIdx = Math.floor((idx - 1) / 2); // (n - 1) / 2
      let parent = this.values[parentIdx];
      if (element <= parent) {
        break;
      } else {
        // swap the values
        this.values[parentIdx] = element;
        this.values[idx] = parent;
        idx = parentIdx; // update the index
      }
    }
    return this.values;
  }

  insert(element) {
    this.values.push(element);
    let result = this.bubbleUp();
    return result;
  }
}

let heap = new MaxBinaryHeap();
console.log(heap.insert(55));
