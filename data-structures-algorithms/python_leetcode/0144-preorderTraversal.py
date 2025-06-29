'''
Difficulty: EASY
No.144    https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Preorder => Root, Left, Right
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution (Recursive approach)
# Time Complexity: O(n), Space Complexity: O(H) where H is the height of the tree
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if root is None: return []

        # define tree
        tree = []

        def traverse(node):
            tree.append(node.val)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        
        traverse(root)

        return tree

# Iterative approach (Eric's Solution)
# Time Complexity: O(n), Space Complexity: O(H) where H is the height of the tree
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []

        if not root: return tree

        # define stack
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            tree.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return tree

            











