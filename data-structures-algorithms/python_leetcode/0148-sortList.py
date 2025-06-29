'''
Difficulty: MEDIUM
No.148    https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution (Runtime: 378ms, Memory: 44.8mb)
# Time Complexity: O(n log n), Space Complexity: O(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None: return None

        # store in list
        temp = []

        current = head

        while current is not None:
            temp.append(current.val)
            current = current.next

        # sort the list
        temp.sort()

        # create an empty linked list
        dummy = ListNode()
        result = dummy
        
        for node in temp:
            result.next = ListNode(node)
            result = result.next

        return dummy.next

# Eric's Solution (uses merge sort - divide and conquer sorting)
# Time Complexity: O(n log n), Space Complexity: O(log k)
# Runtime: 426 ms, Memory: 44.5 MB
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None: return head

        # split list in the middle
        l1 = head
        l2 = self.splitMidNode(head)

        # sort the left list
        l1 = self.sortList(self, l1)

        # sort the right list
        l2 = self.sortList(self, l2)

        # merge the lists together
        dummy = ListNode()
        res = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next

            res = res.next

        if l2 is not None:
            res.next = l2
        else:
            res.next = l1

        return dummy.next

    def splitMidNode(head):
        slow = head
        fast = head
        pre = None

        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        return slow  

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        temp = []
        curr = head
        
        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.sort()

        dummy = ListNode()
        result = dummy

        for nodeVal in temp:
            result.next = ListNode(nodeVal)
            result = result.next

        return dummy.next











