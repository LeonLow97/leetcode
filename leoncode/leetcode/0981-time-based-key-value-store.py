# 981 - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        vals = self.hashmap[key]
        left, right = 0, len(vals) - 1

        while left <= right:
            middle = left + (right - left) // 2
            ts, v = vals[middle]

            if ts == timestamp:
                return v

            if ts < timestamp:
                left = middle + 1
            else:
                right = middle - 1

        return vals[right][1] if right >= 0 else ""