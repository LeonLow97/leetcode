# 124 - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Time: O(N) - we visit each node once
# Space: O(H) - height of the tree, due to recursion stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val

        def dfs(root):
            # base case
            if root is None: return 0

            leftVal = max(dfs(root.left), 0)
            rightVal = max(dfs(root.right), 0)

            self.maxPath = max(self.maxPath, root.val + leftVal + rightVal)

            return root.val + max(leftVal, rightVal)

        dfs(root)
        return self.maxPath