# 105 - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder: left --> root --> right
        # preorder: root --> left --> right

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        # mid is the separation between left subtree and right subtree
        # finding the index where root exists in inorder
        mid = inorder.index(preorder[0])
        
        # construct tree recursively
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
