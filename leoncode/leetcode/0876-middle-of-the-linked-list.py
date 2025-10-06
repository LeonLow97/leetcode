# 876 - https://leetcode.com/problems/middle-of-the-linked-list/

# Time: O(N) - we traverse through the linked list twice, once to find the length and once to find the middle node
# Space: O(1) - we use a constant amount of space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None:
            return None        

        # find len of linked list
        lenList = self.findLen(head)

        # determine the middle node pos of linked list
        mid = lenList // 2

        # define current and count
        current = head
        count = 0

        # traverse through linked list to find middle node
        while current:
            if count == mid: 
                return current
            count += 1
            current = current.next

        # return middle node
        return current

    def findLen(self, head):
        current = head
        count = 0
        
        while current:
            count += 1
            current = current.next

        return count