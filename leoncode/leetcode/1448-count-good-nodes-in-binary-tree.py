# 1448 - https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Time: O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node, maxVal):
            if node is None:
                return

            # count good nodes during DFS traversal
            if node.val >= maxVal:
                self.res += 1
                maxVal = node.val

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return self.res
