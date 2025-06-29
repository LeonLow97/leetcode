'''
Difficulty: MEDIUM
No.142    https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
'''

from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head:  Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None:
            return None
        
        # define slow and fast
        slow = head
        fast = head

        # check if there is a cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # find the length of the cycle
                lenCycle = self.findLen(slow)
                # find the head node of the cycle
                return self.getHeadNode(lenCycle, head)

        # no cycle return null
        return None

    def findLen(self, node): 
        temp = node.next
        size = 1
        while (temp != node):
            temp = temp.next
            size += 1
        return size

    def getHeadNode(self, lenCycle, head):
        # define p1 and p2
        p1 = head
        p2 = head

        # # p2 move len ahead of p1
        for i in range(lenCycle):
            p2 = p2.next
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
                                         
# Create a linked list with a cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

SLL = Solution()
print(SLL.detectCycle(node1).val)  # Output: node2