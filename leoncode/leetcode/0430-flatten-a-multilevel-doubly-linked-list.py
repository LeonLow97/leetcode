# 430 - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Time: O(N)
# Space: O(N) - recursion stack

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)
        return head

    def dfs(self, node):
        # define a pre node
        pre = None

        # iterate through linked list
        while node is not None:
            pre = node

            if node.child:
                tail = self.dfs(node.child)
                tail.next = node.next
                if node.next:
                    node.next.prev = tail
                node.next = node.child
                node.child.prev = node
                node.child = None

                node = tail.next
                pre = tail
            else:
                node = node.next

        return pre