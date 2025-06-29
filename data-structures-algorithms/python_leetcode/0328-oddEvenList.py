'''
Difficulty: Medium
No.328    https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as 
it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Constraints:

- The number of nodes in the linked list is in the range [0, 10^4].
- -10^6 <= Node.val <= 10^6
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None: return head

        # define odd and even list
        oddList = head
        evenList = head.next

        # define current odd and current even (purpose is to keep the head referencing to both lists)
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

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

SLL = Solution()
result = SLL.oddEvenList(node1)

while result:
    print(result.val, end = " -> ")
    result = result.next







