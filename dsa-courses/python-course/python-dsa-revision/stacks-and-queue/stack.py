class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # add to the "head" of the linked list because this is a stack
    def push(self, val):
        newNode = Node(val)

        # no nodes
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            firstElement = self.first
            self.first = newNode
            newNode.next = firstElement

        self.size += 1
        return self.size
    
    # remove the "head" of the linked list
    def pop(self):
        if self.first is None:
            return None
        
        removedNode = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            removedNode.next = None

        self.size -= 1
        return removedNode.val
    
S = Stack()
print(S.push("First"))
print(S.push("Second"))
print(S.push("Third"))
print(S.push("Fourth"))
print(S.pop())