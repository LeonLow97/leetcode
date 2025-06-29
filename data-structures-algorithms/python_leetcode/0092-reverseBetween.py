'''
Difficulty: Medium
No.92    https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right 
where left <= right, reverse the nodes of the list from position left 
to position right, and return the reversed list.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Difficulty: Medium
No.92    https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right 
where left <= right, reverse the nodes of the list from position left 
to position right, and return the reversed list.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution
# Runtime: 32ms, Memory: 14MB
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # base case
        if head is None: return None

        # define current and count
        current = head
        prevLeftNode = None
        afterRightNode = None
        leftNode = None
        count = 1

        # iterate through linked list
        while current is not None:
            if count == left - 1:
                prevLeftNode = current
            if count == left:
                leftNode = current
            if count == right + 1:
                afterRightNode = current

            count += 1
            current = current.next

        reversedLL = self.reverse(leftNode, afterRightNode)
        
        if prevLeftNode:
            prevLeftNode.next = reversedLL
        else:
            head = reversedLL

        if afterRightNode:
            leftNode.next = afterRightNode
        
        if not prevLeftNode and not afterRightNode:
            return reversedLL

        return head
            
    def reverse(self, left, right):
        # define prev and current
        current = left
        prev = None

        # iterate through linked list
        while current != right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

SLL = Solution()
node3 = ListNode(3)
node5 = ListNode(5)
node3.next = node5

result = SLL.reverseBetween(node3, 1, 2)
while result:
    print(result.val)
    result = result.next











