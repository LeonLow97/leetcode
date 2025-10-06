# 543 - https://leetcode.com/problems/diameter-of-binary-tree/

# Time: O(N) - we visit each node once
# Space: O(H) - height of the tree, due to recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(node):
            if node is None:
                return 0
            leftDia = dfs(node.left)
            rightDia = dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, leftDia + rightDia)
            return 1 + max(leftDia, rightDia)

        dfs(root)
        return self.maxDiameter