'''
Difficulty: Medium
No.61    https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
# Runtime: 30 ms, Memory: 13.9 MB
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # number of rotations
        lengthLL = self.findLen(head)
        rotations = k % lengthLL

        # base case
        if head is None: return None
        if rotations == 0: return head

        # define current and count
        current = head
        count = 1
        leftPos = lengthLL - rotations

        newHead = None
        tail = None
        leftNode = None

        # rotate linked list
        while current is not None:
            if count == leftPos:
                leftNode = current
                newHead = current.next
            if count == lengthLL:
                tail = current
            count += 1
            current = current.next

        leftNode.next = None
        tail.next = head

        return newHead

    def findLen(self, head):
        # define counter
        counter = 0
        current = head

        while current is not None:
            counter += 1
            current = current.next

        return counter

SLL = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = SLL.rotateRight(node1, 2)
while result:
    print(result.val, end=" -> ")
    result = result.next












