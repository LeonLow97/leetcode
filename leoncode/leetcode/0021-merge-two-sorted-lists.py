# 21 - https://leetcode.com/problems/merge-two-sorted-lists/

# Time: O(n + m) where n and m are the lengths of the two lists
# Space: O(1) - we are not using any extra space that grows with input
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        if l2 is None: return l1

        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1: current.next = l1
        if l2: current.next = l2

        return dummy.next