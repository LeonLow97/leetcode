# 138 - https://leetcode.com/problems/copy-list-with-random-pointer/

# Time: O(N)
# Space: O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        # key --> original node, value --> clone node
        hashMap = {}
        current = head
        hashMap[current] = Node(current.val)

        while current is not None:
            cloneCurrent = hashMap.get(current)

            # process random node
            if current.random is not None and current.random not in hashMap:
                hashMap[current.random] = Node(current.random.val)
            cloneRandom = hashMap.get(current.random)

            # process next node
            if current.next is not None and current.next not in hashMap:
                hashMap[current.next] = Node(current.next.val)
            cloneNext = hashMap.get(current.next)

            cloneCurrent.random = cloneRandom
            cloneCurrent.next = cloneNext

            current = current.next

        return hashMap.get(head)