'''
Difficulty: MEDIUM
No.143    https://leetcode.com/problems/reorder-list/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # base case
        if head is None: return None
        if head.next is None: return head

        # define slow and fast pointers
        slow = head
        fast = head.next

        # find the middle of the linked list and reverse it
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # separate list into 2 halves and reverse second half
        second = slow.next
        slow.next = None # break the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the 2 halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2