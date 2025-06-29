'''
Difficulty: MEDIUM
No.199    https://leetcode.com/problems/binary-tree-right-side-view/
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue.popleft()

                if node:
                    rightSide = node
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res
