'''
Difficulty: Hard
No.25    https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
# Runtime: 42 ms, Memory: 15.3 MB
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if head is None: 
            return None

        # define count and current
        count = 1
        current = head

        # define empty linked list
        dummy = ListNode()
        pre = dummy

        # nodes
        leftNode = None
        rightNode = None

        # iterate through linked list
        while current is not None:
            if count == 1:
                leftNode = current

            if count == k:
                rightNode = current
                afterRightNode = current.next
                reversedLL = self.reverse(leftNode, rightNode.next)
                pre.next = reversedLL
                pre = leftNode

                current = afterRightNode
                count = 1
                continue
                
            current = current.next
            count += 1

        # in case there are remaining nodes
        # if there are no left-out nodes, the count will be 1.
        if count != 1:
            pre.next = leftNode

        return dummy.next

    def reverse(self, left, right):
        current = left
        pre = None

        while current != right:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre

# Eric's Solution
# Runtime: 47 ms, Memory: 15.2 MB
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if head.next is None: return head
        if k == 1: return head

        # define pre and current
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        current = head

        # reverse the list
        while current is not None:
            space = self.checkHasSpace(k, current)
            if space:
                pre = self.reverse(pre, current, k)
                current = pre.next
            else:
                break

        return dummy.next

    def checkHasSpace(self, k, current):
        for i in range(1, k+1):
            if current is None: return False
            current = current.next
        return True

    def reverse(self, pre, current, k):
        for i in range(0, k):
            temp = current.next
            current.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return current
        






