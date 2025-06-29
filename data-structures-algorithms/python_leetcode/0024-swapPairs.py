from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
# Runtime: 33ms, Memory: 13.9 mb
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None: return head

        # define empty linked list
        dummy = ListNode()
        pre = dummy

        # define count 
        count = 1
        current = head

        leftNode = None
        rightNode = None

        # iterate through linked list
        while current is not None:
            if count == 1:
                leftNode = current

            if count == 2:
                rightNode = current
                afterRightNode = current.next
                reversedLL = self.reverse(leftNode, rightNode.next)
                pre.next = reversedLL
                pre = leftNode

                current = afterRightNode
                count = 1
                continue

            count += 1
            current = current.next

        if count != 1:
            pre.next = leftNode

        return dummy.next

    def reverse(self, left, right):
        # define current and pre
        current = left
        pre = None

        # reverse linked list
        while current != right:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        return pre

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

result = SLL.swapPairs(node1)
while result:
    print(result.val, end = " -> ")
    result = result.next













