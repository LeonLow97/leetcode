# 86 - https://leetcode.com/problems/partition-list/

# Time: O(N) - we traverse through the linked list once
# Space: O(N) - we create 2 new linked lists to store the partitioned
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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