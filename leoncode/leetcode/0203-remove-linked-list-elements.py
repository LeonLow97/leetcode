# 203 - https://leetcode.com/problems/remove-linked-list-elements/

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy.next

        while right is not None:
            if right.val == val:
                left.next = left.next.next
            else:
                left = left.next

            right = right.next

        return dummy.next