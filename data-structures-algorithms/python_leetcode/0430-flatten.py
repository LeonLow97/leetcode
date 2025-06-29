'''
Difficulty: MEDIUM
No.430    https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list, which contains nodes that have a next pointer, 
a previous pointer, and an additional child pointer. This child pointer may or may 
not point to a separate doubly linked list, also containing these special nodes. 
These child lists may have one or more children of their own, and so on, to produce 
a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes 
appear in a single-level, doubly linked list. Let curr be a node with a child list. 
The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Constraints:

- The number of Nodes will not exceed 1000.
- 1 <= Node.val <= 10^5
'''
from typing import Optional

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# Depth First Search (Time complexity: O(n) - number of nodes we have, space complexity: O(1))
class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
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


        