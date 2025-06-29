'''
Difficulty: Easy
No.226    https://leetcode.com/problems/invert-binary-tree/description/
'''

from typing import Optional, TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if root is None: return None

        # swap the children nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive approach for both left and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root