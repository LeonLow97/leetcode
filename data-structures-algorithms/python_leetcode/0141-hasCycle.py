'''
Difficulty: EASY
No.141    https://leetcode.com/problems/linked-list-cycle/
'''

from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True
            
        return False

# Create a linked list with a cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

SLL = Solution()
print(SLL.hasCycle(node1))  # Output: True