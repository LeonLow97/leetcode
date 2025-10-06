# 131 - https://leetcode.com/problems/clone-graph/

# Time: O(N + E) where N is the number of nodes and E is the number of edges in the graph.
# Space: O(N) for the hashmap and the recursion stack.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        nodeToClone = {}

        def dfs(node):
            if node in nodeToClone:
                return nodeToClone[node]
            
            clone = Node(node.val)
            nodeToClone[node] = clone

            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone

        return dfs(node)