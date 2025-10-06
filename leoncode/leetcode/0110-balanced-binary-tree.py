# 110 - https://leetcode.com/problems/balanced-binary-tree/

# Time: O(N) - we visit each node once
# Space: O(H) - the recursion stack can go as deep as the height of the
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        
        def dfs(node):
            if node is None:
                return 0

            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            if abs(rightDepth - leftDepth) > 1:
                self.isBalanced = False
            
            return 1 + max(rightDepth, leftDepth)

        dfs(root)
        return self.isBalanced
