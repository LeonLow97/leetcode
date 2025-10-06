# 212 - https://leetcode.com/problems/word-search-ii/

# Time: O(M * 4 * (3^(L-1))) where M is the number of cells in the board and L is the maximum length of words.
# Space: O(N) where N is the total number of letters in the words list.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.endOfWord = True
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            nextNode = node.children[board[r][c]]
            word = word + board[r][c]
            visited.add((r, c))

            if nextNode.endOfWord:
                res.add(word)
            
            dfs(r+1, c, nextNode, word)
            dfs(r-1, c, nextNode, word)
            dfs(r, c+1, nextNode, word)
            dfs(r, c-1, nextNode, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root, "")

        return list(res)
