# 637 - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Time: O(N^2)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # base case
        if root is None: return []

        queue = []
        visited = []

        queue.append(root)

        while queue:
            size = len(queue)
            sum = 0

            for i in range(size):
                node = queue.pop(0)
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = sum / size
            visited.append(average)

        return visited