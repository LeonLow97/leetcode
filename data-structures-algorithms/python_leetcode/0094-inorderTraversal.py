'''
Difficulty: EASY
No.94    https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

InOrder => Left, Root, Right
'''

from typing import Optional, List

# recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        # define tree
        tree = []

        def traverse(node):
            if node.left: traverse(node.left)
            tree.append(node.val)
            if node.right: traverse(node.right)
        
        traverse(root)

        return tree

# iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []

        if root is None: return tree

        # define stack
        stack = []
        curRoot = root

        while stack or curRoot:

            # append the stack with left nodes
            while curRoot:
                stack.append(curRoot)
                curRoot = curRoot.left

            # check if stack is empty
            if stack is None: break

            # add node to result by popping and re-assign curRoot
            curRoot = stack.pop()
            tree.append(curRoot.val)
            curRoot = curRoot.right

        return tree





















