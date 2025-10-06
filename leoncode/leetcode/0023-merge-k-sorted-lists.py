# 23 - https://leetcode.com/problems/merge-k-sorted-lists/

# Time: O(N log k) where N is the total number of nodes and k is the number of linked lists.
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None: return None
        if len(lists) == 0: return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList = self.mergeTwoLists(l1, l2)
                temp.append(mergedList)
            lists = temp
        
        return lists[0]
    
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