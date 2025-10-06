# 101 - https://leetcode.com/problems/symmetric-tree/

# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None: 
            return True
        
        if left is not None and right is not None:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

        return False