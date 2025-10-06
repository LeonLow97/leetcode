# 98 - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Time: O(n)
# Space: O(h) where h is the height of the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root, float("-inf"), float("inf")])

        while q:
            node, leftEnd, rightEnd = q.popleft()
            if not (leftEnd < node.val < rightEnd):
                return False

            if node.left:
                q.append([node.left, leftEnd, node.val])
            if node.right:
                q.append([node.right, node.val, rightEnd])

        return True