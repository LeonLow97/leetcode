'''
Difficulty: Medium
No.117    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
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

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
