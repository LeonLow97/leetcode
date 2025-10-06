# 2 - https://leetcode.com/problems/add-two-numbers/

# Time: O(max(m, n)) where m and n are the lengths of l1 and l2
# Space: O(max(m, n)) for the output linked list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        if l2 is None: return l1

        dummy = ListNode()
        current = dummy
        carried_over = 0

        while l1 or l2 or carried_over:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            total = l1Val + l2Val + carried_over
            carried_over = total // 10
            val = total % 10

            current.next = ListNode(val)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
