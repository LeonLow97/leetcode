# 160 - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Time: O(N + M) where N and M are the lengths of the two linked lists.
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        if pA is None or pB is None: return None
        
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA