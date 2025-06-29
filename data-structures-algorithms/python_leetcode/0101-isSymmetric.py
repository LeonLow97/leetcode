'''
Difficulty: EASY
No.101    https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution 
# Time complexity: O(n), space complexity: O(n)
# Runtime: 45ms, Memory: 13.9 MB
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None: return True
        if root.left is None and root.right is None: return True

        # extract left and right subtrees
        leftSubTree = root.left
        rightSubTree = root.right
        if leftSubTree is None or rightSubTree is None: return False

        # get list of left and right subtrees
        leftList = self.levelOrder(leftSubTree, "left")
        rightList = self.levelOrder(rightSubTree, "right")

        if leftList != rightList: 
            return False

        return True

    def levelOrder(self, subTree, side):
        queue = []
        visited = []
        queue.append(subTree)

        while queue:
            size = len(queue)

            for i in range(size):
                if side == "left":
                    node = queue.pop(0)

                    if node:
                        visited.append(node.val)

                        if node.left:
                            queue.append(node.left)
                        elif node.left is None:
                            queue.append(None)
                        if node.right:
                            queue.append(node.right)
                        elif node.right is None:
                            queue.append(None)
                    else:
                        visited.append(None)

                elif side == "right":
                    node = queue.pop(0)

                    if node:
                        visited.append(node.val)

                        if node.right:
                            queue.append(node.right)
                        elif node.right is None:
                            queue.append(None)
                        if node.left:
                            queue.append(node.left)
                        elif node.left is None:
                            queue.append(None)
                    else:
                        visited.append(None)
        
        return visited

# Eric's Solution
# Time Complexity: O(N), Space Complexity: O(N)
'''
Space complexity is O(n) because it uses a recursive approach. In each call to the `isMirror` function,
it creates a new stack frame on the call stack. The maximum call stack is equal to the height of the binary
tree, where log(n) is the base case and o(n) is the worst case.
'''
# Runtime: 42ms, Memory: 13.8 MB
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None: 
            return True
        
        if left is not None and right is not None:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

        return False
