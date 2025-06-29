'''
Difficulty: MEDIUM
No.708    https://leetcode.com/problems/copy-list-with-random-pointer/
'''

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Using a hashmap to keep the location of the node in memory
# Runtime: 26ms, Memory: 15.1
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # base case
        if head is None:
            return None

        #  define hash map
        hm = {}
        current = head
        hm[current] = Node(current.val)

        while current is not None:
            # get new node of current pointer
            currentClone = hm.get(current)

            if current.random is not None and current.random not in hm:
                hm[current.random] = Node(current.random.val)
            randomClone = hm.get(current.random)

            currentClone.random = randomClone

            # add next node if it does not exist in hm
            if current.next is not None and current.next not in hm:
                hm[current.next] = Node(current.next.val)
            nextClone = hm.get(current.next)

            currentClone.next = nextClone

            current = current.next

        return hm.get(head)







