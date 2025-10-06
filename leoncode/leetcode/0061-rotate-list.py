# 61 - https://leetcode.com/problems/rotate-list/

# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if head is None: return None

        # number of rotations
        lengthLL = self.findLen(head)
        rotations = k % lengthLL

        if rotations == 0: return head

        # define current and count
        current = head
        count = 1
        leftPos = lengthLL - rotations

        newHead = None
        tail = None
        leftNode = None

        # rotate linked list
        while current is not None:
            if count == leftPos:
                leftNode = current
                newHead = current.next
            if count == lengthLL:
                tail = current
            count += 1
            current = current.next

        leftNode.next = None
        tail.next = head

        return newHead

    def findLen(self, head):
        # define counter
        counter = 0
        current = head

        while current is not None:
            counter += 1
            current = current.next

        return counter
