'''
Difficulty: MEDIUM
No.2    https://leetcode.com/problems/add-two-numbers/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy linked list
        dummy = ListNode()
        current = dummy
        carriedOver = 0

        while l1 or l2 or carriedOver:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carriedOver
            carriedOver = sum // 10
            nodeVal = sum % 10

            current.next = ListNode(nodeVal)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next