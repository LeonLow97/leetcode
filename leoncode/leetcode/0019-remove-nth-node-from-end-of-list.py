# 19 - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Time: O(L) - L is the length of the linked list
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        for _ in range(n):
            current = current.next

        prev = dummy
        while current.next:
            prev = prev.next
            current = current.next
        
        prev.next = prev.next.next
        return dummy.next