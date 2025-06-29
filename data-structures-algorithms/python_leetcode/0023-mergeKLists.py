'''
Difficulty: Hard
No.23    https://www.youtube.com/watch?v=L-8LVBPmIpc&list=PL1MJrDFRFiKai5yk1cx6C26qS57Y1AHYR&index=7&ab_channel=EricProgramming

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity O(n log k)
# n for iterating through all the lists
# k for merging 2 lists at once
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if not lists or len(lists) == 0:
            return  None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None ## could have odd number of lists
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        # merging 2 linked lists
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

        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next

# Another Solution (Cleaner)
# Time Complexity: O(n log n), Runtime: 95 ms, Memory: 18.3 MB
# n for going through the list
# log n for sorting
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if lists is None or len(lists) == 0:
            return None

        mergedList = []
        for current in lists:
            while current:
                mergedList.append(current.val)
                current = current.next

        # sort the mergedList
        mergedList.sort()

        # define empty linked list
        dummy = ListNode()
        current = dummy
        counter = 0

        while counter < len(mergedList):
            val = mergedList[counter]
            current.next = ListNode(val)
            counter += 1
            current = current.next

        return dummy.next
            



