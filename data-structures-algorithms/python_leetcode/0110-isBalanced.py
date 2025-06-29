'''
Difficulty: Easy
No.110    https://leetcode.com/problems/balanced-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        # depth first search (recursive)
        def dfs(root):
            # [is this a balanced tree/subtree?, height of tree]
            if root is None: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]