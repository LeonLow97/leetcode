# 24 - https://leetcode.com/problems/swap-nodes-in-pairs/

# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None: return head

        # define empty linked list
        dummy = ListNode()
        pre = dummy

        # define count 
        count = 1
        current = head

        leftNode = None
        rightNode = None

        # iterate through linked list
        while current is not None:
            if count == 1:
                leftNode = current

            if count == 2:
                rightNode = current
                afterRightNode = current.next
                reversedLL = self.reverse(leftNode, rightNode.next)
                pre.next = reversedLL
                pre = leftNode

                current = afterRightNode
                count = 1
                continue

            count += 1
            current = current.next

        if count != 1:
            pre.next = leftNode

        return dummy.next

    def reverse(self, left, right):
        # define current and pre
        current = left
        pre = None

        # reverse linked list
        while current != right:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre