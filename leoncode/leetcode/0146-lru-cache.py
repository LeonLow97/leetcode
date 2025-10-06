# 146 - https://leetcode.com/problems/lru-cache/

# Time: O(1) for both get and put
# Space: O(capacity)

class Node:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key, self.value = key, value
        self.next, self.prev = next, prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head, self.tail = Node(), Node() # head is MRU and tail is LRU
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def insert(self, node):
        p, n = self.head, self.head.next
        p.next, n.prev = node, node
        node.next, node.prev = n, p

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # make node MRU
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.cap:
                # evict lru
                lruNode = self.tail.prev
                del self.cache[lruNode.key]
                self.remove(lruNode)
            newNode = Node(key, value)
            self.insert(newNode)
            self.cache[key] = newNode