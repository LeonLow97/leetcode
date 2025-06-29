class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.values = []

    # add node to the end of the list
    def enqueue(self, val, priority):
        newNode = Node(val, priority)
        self.values.append(newNode)
        self.bubbleUp()

    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]
            if element.priority >= parent.priority: break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx

    def dequeue(self):
        min = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sinkDown()
        if min.val:
            return min.val
        else: 
            return None

    def sinkDown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            leftChild, rightChild = None, None
            swap = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild.priority < element.priority:
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if ((swap is None and rightChild.priority < element.priority) or (swap is not None and rightChild.priority < leftChild.priority)):
                    swap = rightChildIdx

            if swap is None: break

            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

ER = PriorityQueue()
ER.enqueue("common cold", 5)
ER.enqueue("gunshot wound", 1)
ER.enqueue("high fever", 4)
ER.enqueue("broken arm", 2)
ER.enqueue("glass in foot", 3)

print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())







