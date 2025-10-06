# 127 - https://leetcode.com/problems/word-ladder/

# Time: O(M * N) where M is the length of each word and N is the number of words in the wordList.
# Space: O(M * N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjList = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjList[pattern].append(word)

        visited = set([beginWord])
        q = collections.deque([beginWord])
        numWords = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return numWords
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for patternWord in adjList[pattern]:
                        if patternWord not in visited:
                            q.append(patternWord)
                            visited.add(patternWord)
            numWords += 1
        return 0