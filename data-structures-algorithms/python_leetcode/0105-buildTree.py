'''
Difficulty: Medium
No.105    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Neetcode's Solution (recursive approach)
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # base case
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])

        # Retrieving the index of the root in inorder
        mid = inorder.index(preorder[0])

        # Recursive approach 
        # For left tree, start with index 1 for preorder because index 0 is root 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root