# 328 - https://leetcode.com/problems/odd-even-linked-list/

# Time: O(n) - we traverse the entire linked list once
# Space: O(1) - we use constant space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None: return head

        # define odd and even list
        oddList = head
        evenList = head.next

        # define current odd and current even
        currentOdd = oddList
        currentEven = evenList

        while currentOdd.next is not None and currentEven.next is not None:
            # gather the odd list
            currentOdd.next = currentEven.next
            currentOdd = currentOdd.next

            # gather the even list
            currentEven.next = currentOdd.next
            currentEven = currentEven.next

        currentOdd.next = evenList
            
        return oddList