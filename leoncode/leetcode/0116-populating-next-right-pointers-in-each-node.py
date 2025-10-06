# 116 - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # base case
        if root is None: return None

        queue = []
        queue.append(root)

        while queue:
            size = len(queue)
            pre = None
            for i in range(size):
                node = queue.pop(0)

                if pre is not None:
                    pre.next = node

                pre = node

                # because we have a perfect binary tree
                if node.left is not None:
                    queue.append(node.left)
                    queue.append(node.right)
                
        return root