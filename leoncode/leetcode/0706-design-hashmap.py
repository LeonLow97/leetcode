# 706 - https://leetcode.com/problems/design-hashmap/

class Node:
    def __init__(self, key=0, value=0, next=None):
        self.next = next
        self.key, self.value = key, value

class MyHashMap:
    def __init__(self):
        self.cap = 1000
        self.hm = [Node() for _ in range(self.cap)]

    def hash(self, key):
        return key % self.cap

    def put(self, key: int, value: int) -> None:
        hash_val = self.hash(key)
        current = self.hm[hash_val]
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        current.next = Node(key, value)

    def get(self, key: int) -> int:
        hash_val = self.hash(key)
        current = self.hm[hash_val].next
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        hash_val = self.hash(key)
        current = self.hm[hash_val]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next