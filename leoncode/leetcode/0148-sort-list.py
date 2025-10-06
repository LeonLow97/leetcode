# 148 - https://leetcode.com/problems/sort-list/

# Time: O(n log n)
# Space: O(log n) - recursion stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge Sort
        if not head or head.next is None:
            return head

        # get mid of linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left_arr, right_arr = head, slow.next
        slow.next = None

        left_arr = self.sortList(left_arr)
        right_arr = self.sortList(right_arr)

        merged_list = self.mergeTwoLists(left_arr, right_arr)
        return merged_list
    
    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1

        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
    
        if l1: current.next = l1
        if l2: current.next = l2

        return dummy.next