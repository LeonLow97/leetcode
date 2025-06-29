'''
Difficulty: Easy
No.876    https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:

- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution (Runtime: 33 ms, Beats 85.1%)
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

def create_linked_list(values):
    node = ListNode(values[0])
    head = node

    for value in values[1:]:
        node.next = ListNode(value)
        node = node.next

    return head

values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

values1 = [1, 2, 3, 4, 5, 6]
head1 = create_linked_list(values1)

result = Solution().middleNode(head) # 3 -> 4 -> 5
result1 = Solution().middleNode(head1) # 4 -> 5 -> 6

while result:
    print(result.val, end = " -> ")
    result = result.next
print()

while result1:
    print(result1.val, end = " -> ")
    result1 = result1.next
print()