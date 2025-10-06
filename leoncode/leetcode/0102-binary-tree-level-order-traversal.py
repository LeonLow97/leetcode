# 102 - https://leetcode.com/problems/binary-tree-level-order-traversal/

# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None: return res

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            temp = []
            for _ in range(qLen):
                node = q.popleft()
                temp.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(temp)

        return res
