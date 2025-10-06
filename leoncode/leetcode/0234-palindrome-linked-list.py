# 234 - https://leetcode.com/problems/palindrome-linked-list/

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution with constant space complexity
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # base case
        if head is None or head.next is None: return True

        # define slow and fast pointers
        slow = head
        fast = head

        # traverse through the linked list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # define left and right pointers
        left = head
        right = self.reverse(slow)

        while right is not None:
            if (left.val == right.val):
                left = left.next
                right = right.next
            else:
                return False

        return True

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        
        # define pointers
        current = head
        prev = None

        # reverse the LL
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev