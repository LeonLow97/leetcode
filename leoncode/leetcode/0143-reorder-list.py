# 143 - https://leetcode.com/problems/reorder-list/

# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None: return None
        if head.next is None: return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of linked list
        prev = None
        current = slow.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        slow.next = None

        first, second = head, prev
        
        while first and second:
            firstNext, secondNext = first.next, second.next
            first.next, second.next = second, firstNext
            first, second = firstNext, secondNext