# 106 - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not inorder or not postorder: return None

        # Create the root using TreeNode
        root = TreeNode(postorder.pop())

        # Retrieve mid index in inorder
        mid = inorder.index(root.val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:])

        return root