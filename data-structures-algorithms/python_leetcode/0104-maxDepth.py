'''
Difficulty: Easy
No.104    https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from typing import Optional, TreeNode
from collections import deque

# DFS (recursive), Time Complexity: O(n), Space complexity: O(H)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS (iterative), using deque, Time Complexity: O(n) 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        level = 0
        q = deque([root])
        while q:

            # remove whatever is in the queue and replace
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1

        return level

# DFS (iterative), using a stack, add node and depth to the stack
# preorder DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            # to ignore nodes that are None
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1]) # even if nodes are None, we add them
                stack.append([node.right, depth + 1])

        return res