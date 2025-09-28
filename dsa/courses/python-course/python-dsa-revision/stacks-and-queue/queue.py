class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self, first, last, size):
        self.first = first
        self.last = last
        self.size = 0

    # add a node to the end of the queue
    def enqueue(self, val):
        newNode = Node(val)

        # check for existing first node
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
        return self.size
    
    # remove a node from the start of the queue
    def dequeue(self):
        # check for existing first node
        if self.first is None:
            return None
        
        removedNode = self.first
        # if first node exists, check if node is one and only node
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        removedNode.next = None
        self.size -= 1
        return removedNode.val
    
# create an empty queue
q = Queue(None, None, 0)

# add some nodes to the queue
print(q.enqueue(1))  # returns 1 (size of the queue)
print(q.enqueue(2))  # returns 2
print(q.enqueue(3))  # returns 3

# remove a node from the queue
print(q.dequeue())   # returns 1 (the value of the removed node)

# add some more nodes to the queue
print(q.enqueue(4))  # returns 3 (the size of the queue)

# remove all nodes from the queue
print(q.dequeue())   # returns 2
print(q.dequeue())   # returns 3
print(q.dequeue())   # returns 4
print(q.dequeue())   # returns None (since the queue is empty)
