# 142 - https://leetcode.com/problems/linked-list-cycle-ii/

# Time: O(N)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head:  Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None:
            return None
        
        # define slow and fast
        slow = head
        fast = head

        # check if there is a cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # find the length of the cycle
                lenCycle = self.findLen(slow)
                # find the head node of the cycle
                return self.getHeadNode(lenCycle, head)

        # no cycle return false
        return None

    def findLen(self, node): 
        temp = node.next
        size = 1
        while (temp != node):
            temp = temp.next
            size += 1
        return size

    def getHeadNode(self, lenCycle, head):
        # define p1 and p2
        p1 = head
        p2 = head

        # # p2 move len ahead of p1
        for i in range(lenCycle):
            p2 = p2.next
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
        