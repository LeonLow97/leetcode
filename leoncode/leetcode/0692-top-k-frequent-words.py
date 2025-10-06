# 692 - https://leetcode.com/problems/top-k-frequent-words/

# Time: O(N + M log M) where N is the number of words and M is the number of unique words
# Space: O(N)

from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        buckets = [[] for _ in range(n + 1)]

        wordToCount = {}
        for word in words:
            wordToCount[word] = wordToCount.get(word, 0) + 1
        
        for word, count in wordToCount.items():
            buckets[count].append(word)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for word in sorted(buckets[i]):  # Sort lexicographically
                    res.append(word)
                    if len(res) == k:
                        return res
        
        return res