# 705 - https://leetcode.com/problems/design-hashset/

class MyHashSet:
    def __init__(self):
        self.cap = 1000
        self.hs = [[] for _ in range(self.cap)]

    def _hash(self, key):
        return key % self.cap

    def add(self, key: int) -> None:
        hash_val = self._hash(key)
        if key not in self.hs[hash_val]:
            self.hs[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        if key in self.hs[hash_val]:
            self.hs[hash_val].remove(key)

    def contains(self, key: int) -> bool:
        hash_val = self._hash(key)
        return key in self.hs[hash_val]