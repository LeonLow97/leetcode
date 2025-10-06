# 117 - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Time: O(N)
# Space: O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # base case
        if root is None: return None

        queue = []
        queue.append(root)

        while queue:
            pre = None
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                if pre is not None:
                    pre.next = node

                pre = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


