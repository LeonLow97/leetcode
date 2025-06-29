'''
Difficulty: Easy
No.160    https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Given the heads of two singly linked-lists headA and headB, return the 
node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution (165ms, 29.6MB)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # define pointers
        pA = headA
        pB = headB

        # find length of both linked lists
        lenA = self.findLen(headA)
        lenB = self.findLen(headB)

        # find the difference between the lengths
        if lenA > lenB:
            diffLen = lenA - lenB
            for i in range(diffLen):
                pA = pA.next
            while pA is not None:
                if pA.val == pB.val and pA == pB:
                    return pA
                pA = pA.next
                pB = pB.next
        else:
            diffLen = lenB - lenA
            for i in range(diffLen):
                pB = pB.next
            while pB is not None:
                if pA.val == pB.val and pA == pB:
                    return pB
                pA = pA.next
                pB = pB.next

        return None

    def findLen(self, head):
        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

# Tutor's Solution
# Time Complexity: O(A + B), Space Complexity: O(1)
# 147ms and 29.4MB
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        if pA is None or pB is None: return None
        
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA


node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

SLL = Solution()
print(SLL.findLen(node1))










