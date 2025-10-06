# 211 - https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Time: O(N) 
# Space: O(N)

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, wordPos):
            cur = node
            for i in range(wordPos, len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(child, i+1):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.endOfWord

        return dfs(self.root, 0)