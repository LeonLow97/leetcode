'''
Difficulty: MEDIUM
No.1448    https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # depth first search
        def dfs(node, maxVal):
            if node is None: return 0

            if node.val >= maxVal: res = 1
            else: res = 0

            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)