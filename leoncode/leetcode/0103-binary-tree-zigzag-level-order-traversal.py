# 103 - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Time: O(N)
# Space: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if root is None: return []

        queue = []
        visited = []
        current = root
        zigzag = False

        queue.append(current)

        while queue:
            size = len(queue)
            sub = []
            for i in range(size):
                node = queue.pop(0)

                if ~zigzag:
                    sub.append(node.val)
                else:
                    sub.insert(0, node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            zigzag = ~zigzag
            visited.append(sub)

        return visited 