
class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    # Insert element at the end and bubble up to the top (correct spot)
    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]

        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]

            if element <= parent:
                break
            else:
                self.values[parentIdx] = element
                self.values[idx] = parent
                idx = parentIdx

        return self.values

    def insert(self, element):
        self.values.append(element)
        result = self.bubbleUp()
        return result

    def extractMax(self):
        max = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sinkDown()
        return max
    
    def sinkDown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            leftChild = None
            rightChild = None
            swap = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild > element:
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if ((swap is None and rightChild > element) or (swap is not None and rightChild > leftChild)):
                    swap = rightChildIdx

            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

heap = MaxBinaryHeap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.insert(55)

print(heap.extractMax())
print(heap.values) # [41, 39, 33, 18, 27, 12]

print(heap.extractMax())
print(heap.values) # [39, 27, 33, 18, 12]

print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())

heap.insert(55)
print(heap.extractMax())