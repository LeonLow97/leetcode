'''
Difficulty: MEDIUM
No.86    https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all 
nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution 
# Time Complexity: O(n), Runtime: 35ms, Memory: 13.8 MB, Space Complexity: O(1)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # base case
        if head is None: return None

        # create 2 empty linked lists
        l1 = ListNode()
        dummy1 = l1
        l2 = ListNode()
        dummy2 = l2

        # define head and partition pointer
        current = head

        # traverse through linked list
        while current is not None:
            if current.val < x:
                dummy1.next = ListNode(current.val)
                dummy1 = dummy1.next
            elif current.val >= x:
                dummy2.next = ListNode(current.val)
                dummy2 = dummy2.next
            
            current = current.next

        dummy1.next = l2.next
        dummy2.next = None

        return l1.next

# Eric's Solution (Similar to mine)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        # define pointers
        d1 = ListNode()
        d2 = ListNode()
        low = d1
        high = d2

        current = head

        while current is not None:
            if current.val < x:
                low.next = current
                low = current
            else:
                high.next = current
                high = current

            current = current.next

        # merge two pointer
        low.next = d2.next
        high.next = None

        return d1.next







