'''
Difficulty: Easy
No.234    https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Constraints:

- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution with constant space complexity
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # base case
        if head is None or head.next is None: return True

        # define slow and fast pointers
        slow = head
        fast = head

        # traverse through linked list
        while fast is not None and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next

        # reverse the the last half of the linked list
        left = head
        right = self.reverse(slow)

        # check if it is palindrome
        while right is not None:
            if (left.val == right.val):
                left = left.next
                right = right.next
            else: 
                return False

        return True

    def reverse(self, head):
        # base case 
        if head is None or head.next is None:
            return head

        # reverse
        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

SLL = Solution()
print(SLL.isPalindrome(node1))

## Another Solution that is not constant space complexity
## Compare the head original linked list with the 
## head of the reverse linked list