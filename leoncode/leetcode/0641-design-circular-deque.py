# 641 - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next, self.prev = next, prev

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = None, None
        self.cap = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.head = self.head.next
        if self.head is None:
            self.head = self.tail = None
        else:
            self.head.prev = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.tail = self.tail.prev
        if self.tail is None:
            self.tail = self.head = None
        else:
            self.tail.next = None
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.head.value

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap