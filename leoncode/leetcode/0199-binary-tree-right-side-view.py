# 199 - https://leetcode.com/problems/binary-tree-right-side-view/

# Time: O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None: return res

        q = deque()
        q.append(root)

        while q:
            res.append(q[-1].val)
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res
